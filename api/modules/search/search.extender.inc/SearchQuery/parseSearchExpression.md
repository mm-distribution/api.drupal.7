# SearchQuery::parseSearchExpression()

- **Type:** Method
- **File:** [`modules/search/search.extender.inc`](../_file.md), lines 197–320 · [local source](../../../../../source/modules/search/search.extender.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.extender.inc#L197-L320)
- **Class:** [SearchQuery](../SearchQuery.md)
- **Module/theme:** search

## Signature

```php
protected function parseSearchExpression()
```

## Documentation

```text
Parses the search query into SQL conditions.

We build two queries that match the dataset bodies.
```

## Code

```php
  protected function parseSearchExpression() {
    // Matchs words optionally prefixed by a dash. A word in this case is
    // something between two spaces, optionally quoted.
    preg_match_all('/ (-?)("[^"]+"|[^" ]+)/i', ' ' .  $this->searchExpression , $keywords, PREG_SET_ORDER);

    if (count($keywords) ==  0) {
      return;
    }

    // Classify tokens.
    $or = FALSE;
    $warning = '';
    $limit_combinations = variable_get('search_and_or_limit', 7);
    // The first search expression does not count as AND.
    $and_count = -1;
    $or_count = 0;
    foreach ($keywords as $match) {
      if ($or_count && $and_count + $or_count >= $limit_combinations) {
        // Ignore all further search expressions to prevent Denial-of-Service
        // attacks using a high number of AND/OR combinations.
        $this->expressionsIgnored = TRUE;
        break;
      }
      $phrase = FALSE;
      // Strip off phrase quotes.
      if ($match[2][0] == '"') {
        $match[2] = substr($match[2], 1, -1);
        $phrase = TRUE;
        $this->simple = FALSE;
      }
      // Simplify keyword according to indexing rules and external
      // preprocessors. Use same process as during search indexing, so it
      // will match search index.
      $words = search_simplify($match[2]);
      // Re-explode in case simplification added more words, except when
      // matching a phrase.
      $words = $phrase ? array($words) : preg_split('/ /', $words, -1, PREG_SPLIT_NO_EMPTY);
      // Negative matches.
      if ($match[1] == '-') {
        $this->keys['negative'] = array_merge($this->keys['negative'], $words);
      }
      // OR operator: instead of a single keyword, we store an array of all
      // OR'd keywords.
      elseif ($match[2] == 'OR' && count($this->keys['positive'])) {
        $last = array_pop($this->keys['positive']);
        // Starting a new OR?
        if (!is_array($last)) {
          $last = array($last);
        }
        $this->keys['positive'][] = $last;
        $or = TRUE;
        $or_count++;
        continue;
      }
      // AND operator: implied, so just ignore it.
      elseif ($match[2] == 'AND' || $match[2] == 'and') {
        $warning = $match[2];
        continue;
      }

      // Plain keyword.
      else {
        if ($match[2] == 'or') {
          $warning = $match[2];
        }
        if ($or) {
          // Add to last element (which is an array).
          $this->keys['positive'][count($this->keys['positive']) - 1] = array_merge($this->keys['positive'][count($this->keys['positive']) - 1], $words);
        }
        else {
          $this->keys['positive'] = array_merge($this->keys['positive'], $words);
          $and_count++;
        }
      }
      $or = FALSE;
    }

    // Convert keywords into SQL statements.
    $this->conditions = db_and();
    $simple_and = FALSE;
    $simple_or = FALSE;
    // Positive matches.
    foreach ($this->keys['positive'] as $key) {
      // Group of ORed terms.
      if (is_array($key) && count($key)) {
        $simple_or = TRUE;
        $any = FALSE;
        $queryor = db_or();
        foreach ($key as $or) {
          list($num_new_scores) = $this->parseWord($or);
          $any |= $num_new_scores;
          $queryor->condition('d.data', "% $or %", 'LIKE');
        }
        if (count($queryor)) {
          $this->conditions->condition($queryor);
          // A group of OR keywords only needs to match once.
          $this->matches += ($any > 0);
        }
      }
      // Single ANDed term.
      else {
        $simple_and = TRUE;
        list($num_new_scores, $num_valid_words) = $this->parseWord($key);
        $this->conditions->condition('d.data', "% $key %", 'LIKE');
        if (!$num_valid_words) {
          $this->simple = FALSE;
        }
        // Each AND keyword needs to match at least once.
        $this->matches += $num_new_scores;
      }
    }
    if ($simple_and && $simple_or) {
      $this->simple = FALSE;
    }
    // Negative matches.
    foreach ($this->keys['negative'] as $key) {
      $this->conditions->condition('d.data', "% $key %", 'NOT LIKE');
      $this->simple = FALSE;
    }

    if ($warning == 'or') {
      drupal_set_message(t('Search for either of the two terms with uppercase <strong>OR</strong>. For example, <strong>cats OR dogs</strong>.'));
    }
  }
```

---
_Drupal 7.103 · [modules/search/search.extender.inc](https://github.com/drupal/drupal/blob/7.103/modules/search/search.extender.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
