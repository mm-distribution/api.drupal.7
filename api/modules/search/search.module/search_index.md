# search_index()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 554–775 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L554-L775)
- **Module/theme:** search
- **Topics:** [search](../../../topics/search.md)

## Signature

```php
function search_index($sid, $module, $text)
```

## Documentation

```text
Update the full-text search index for a particular item.

@param $sid
  An ID number identifying this particular item (e.g., node ID).
@param $module
  The machine-readable name of the module that this item comes from (a module
  that implements hook_search_info()).
@param $text
  The content of this item. Must be a piece of HTML or plain text.

@ingroup search
```

## Code

```php
function search_index($sid, $module, $text) {
  $minimum_word_size = variable_get('minimum_word_size', 3);

  // Link matching
  global $base_url;
  $node_regexp = '@href=[\'"]?(?:' . preg_quote($base_url, '@') . '/|' . preg_quote(base_path(), '@') . ')(?:\?q=)?/?((?![a-z]+:)[^\'">]+)[\'">]@i';

  // Multipliers for scores of words inside certain HTML tags. The weights are stored
  // in a variable so that modules can overwrite the default weights.
  // Note: 'a' must be included for link ranking to work.
  $tags = variable_get('search_tag_weights', array(
    'h1' => 25,
    'h2' => 18,
    'h3' => 15,
    'h4' => 12,
    'h5' => 9,
    'h6' => 6,
    'u' => 3,
    'b' => 3,
    'i' => 3,
    'strong' => 3,
    'em' => 3,
    'a' => 10));

  // Strip off all ignored tags to speed up processing, but insert space before/after
  // them to keep word boundaries.
  $text = str_replace(array('<', '>'), array(' <', '> '), $text);
  $text = strip_tags($text, '<' . implode('><', array_keys($tags)) . '>');

  // Split HTML tags from plain text.
  $split = preg_split('/\s*<([^>]+?)>\s*/', $text, -1, PREG_SPLIT_DELIM_CAPTURE);
  // Note: PHP ensures the array consists of alternating delimiters and literals
  // and begins and ends with a literal (inserting $null as required).

  $tag = FALSE; // Odd/even counter. Tag or no tag.
  $link = FALSE; // State variable for link analyzer
  $score = 1; // Starting score per word
  $accum = ' '; // Accumulator for cleaned up data
  $tagstack = array(); // Stack with open tags
  $tagwords = 0; // Counter for consecutive words
  $focus = 1; // Focus state

  $results = array(0 => array()); // Accumulator for words for index

  foreach ($split as $value) {
    if ($tag) {
      // Increase or decrease score per word based on tag
      list($tagname) = explode(' ', $value, 2);
      $tagname = drupal_strtolower($tagname);
      // Closing or opening tag?
      if ($tagname[0] == '/') {
        $tagname = substr($tagname, 1);
        // If we encounter unexpected tags, reset score to avoid incorrect boosting.
        if (!count($tagstack) || $tagstack[0] != $tagname) {
          $tagstack = array();
          $score = 1;
        }
        else {
          // Remove from tag stack and decrement score
          $score = max(1, $score - $tags[array_shift($tagstack)]);
        }
        if ($tagname == 'a') {
          $link = FALSE;
        }
      }
      else {
        if (isset($tagstack[0]) && $tagstack[0] == $tagname) {
          // None of the tags we look for make sense when nested identically.
          // If they are, it's probably broken HTML.
          $tagstack = array();
          $score = 1;
        }
        else {
          // Add to open tag stack and increment score
          array_unshift($tagstack, $tagname);
          $score += $tags[$tagname];
        }
        if ($tagname == 'a') {
          // Check if link points to a node on this site
          if (preg_match($node_regexp, $value, $match)) {
            $path = drupal_get_normal_path($match[1]);
            if (preg_match('!(?:node|book)/(?:view/)?([0-9]+)!i', $path, $match)) {
              $linknid = $match[1];
              if ($linknid > 0) {
                $node = db_query('SELECT title, nid, vid FROM {node} WHERE nid = :nid', array(':nid' => $linknid), array('target' => 'slave'))->fetchObject();
                $link = TRUE;
                $linktitle = $node->title;
              }
            }
          }
        }
      }
      // A tag change occurred, reset counter.
      $tagwords = 0;
    }
    else {
      // Note: use of PREG_SPLIT_DELIM_CAPTURE above will introduce empty values
      if ($value != '') {
        if ($link) {
          // Check to see if the node link text is its URL. If so, we use the target node title instead.
          if (preg_match('!^https?://!i', $value)) {
            $value = $linktitle;
          }
        }
        $words = search_index_split($value);
        foreach ($words as $word) {
          // Add word to accumulator
          $accum .= $word . ' ';
          // Check wordlength
          if (is_numeric($word) || drupal_strlen($word) >= $minimum_word_size) {
            // Links score mainly for the target.
            if ($link) {
              if (!isset($results[$linknid])) {
                $results[$linknid] = array();
              }
              $results[$linknid][] = $word;
              // Reduce score of the link caption in the source.
              $focus *= 0.2;
            }
            // Fall-through
            if (!isset($results[0][$word])) {
              $results[0][$word] = 0;
            }
            $results[0][$word] += $score * $focus;

            // Focus is a decaying value in terms of the amount of unique words up to this point.
            // From 100 words and more, it decays, to e.g. 0.5 at 500 words and 0.3 at 1000 words.
            $focus = min(1, .01 + 3.5 / (2 + count($results[0]) * .015));
          }
          $tagwords++;
          // Too many words inside a single tag probably mean a tag was accidentally left open.
          if (count($tagstack) && $tagwords >= 15) {
            $tagstack = array();
            $score = 1;
          }
        }
      }
    }
    $tag = !$tag;
  }

  search_reindex($sid, $module, TRUE);

  // Insert cleaned up data into dataset
  db_insert('search_dataset')
    ->fields(array(
      'sid' => $sid,
      'type' => $module,
      'data' => $accum,
      'reindex' => 0,
    ))
    ->execute();

  // Insert results into search index
  foreach ($results[0] as $word => $score) {
    // If a word already exists in the database, its score gets increased
    // appropriately. If not, we create a new record with the appropriate
    // starting score.
    db_merge('search_index')
      ->key(array(
        'word' => $word,
        'sid' => $sid,
        'type' => $module,
      ))
      ->fields(array('score' => $score))
      ->expression('score', 'score + :score', array(':score' => $score))
      ->execute();
    search_dirty($word);
  }
  unset($results[0]);

  // Get all previous links from this item.
  $result = db_query("SELECT nid, caption FROM {search_node_links} WHERE sid = :sid AND type = :type", array(
    ':sid' => $sid,
    ':type' => $module
  ), array('target' => 'slave'));
  $links = array();
  foreach ($result as $link) {
    $links[$link->nid] = $link->caption;
  }

  // Now store links to nodes.
  foreach ($results as $nid => $words) {
    $caption = implode(' ', $words);
    if (isset($links[$nid])) {
      if ($links[$nid] != $caption) {
        // Update the existing link and mark the node for reindexing.
        db_update('search_node_links')
          ->fields(array('caption' => $caption))
          ->condition('sid', $sid)
          ->condition('type', $module)
          ->condition('nid', $nid)
          ->execute();
        search_touch_node($nid);
      }
      // Unset the link to mark it as processed.
      unset($links[$nid]);
    }
    elseif ($sid != $nid || $module != 'node') {
      // Insert the existing link and mark the node for reindexing, but don't
      // reindex if this is a link in a node pointing to itself.
      db_insert('search_node_links')
        ->fields(array(
          'caption' => $caption,
          'sid' => $sid,
          'type' => $module,
          'nid' => $nid,
        ))
        ->execute();
      search_touch_node($nid);
    }
  }
  // Any left-over links in $links no longer exist. Delete them and mark the nodes for reindexing.
  foreach ($links as $nid => $caption) {
    db_delete('search_node_links')
      ->condition('sid', $sid)
      ->condition('type', $module)
      ->condition('nid', $nid)
      ->execute();
    search_touch_node($nid);
  }
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
