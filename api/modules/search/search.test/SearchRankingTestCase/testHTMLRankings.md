# SearchRankingTestCase::testHTMLRankings()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 473–550 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L473-L550)
- **Class:** [SearchRankingTestCase](../SearchRankingTestCase.md)
- **Module/theme:** search

## Signature

```php
function testHTMLRankings()
```

## Documentation

```text
Test rankings of HTML tags.
```

## Code

```php
  function testHTMLRankings() {
    // Login with sufficient privileges.
    $this->drupalLogin($this->drupalCreateUser(array('create page content')));

    // Test HTML tags with different weights.
    $sorted_tags = array('h1', 'h2', 'h3', 'h4', 'a', 'h5', 'h6', 'notag');
    $shuffled_tags = $sorted_tags;

    // Shuffle tags to ensure HTML tags are ranked properly.
    shuffle($shuffled_tags);
    $settings = array(
      'type' => 'page',
      'title' => 'Simple node',
    );
    foreach ($shuffled_tags as $tag) {
      switch ($tag) {
        case 'a':
          $settings['body'] = array(LANGUAGE_NONE => array(array('value' => l('Drupal Rocks', 'node'), 'format' => 'full_html')));
          break;
        case 'notag':
          $settings['body'] = array(LANGUAGE_NONE => array(array('value' => 'Drupal Rocks')));
          break;
        default:
          $settings['body'] = array(LANGUAGE_NONE => array(array('value' => "<$tag>Drupal Rocks</$tag>", 'format' => 'full_html')));
          break;
      }
      $nodes[$tag] = $this->drupalCreateNode($settings);
    }

    // Update the search index.
    module_invoke_all('update_index');
    search_update_totals();

    // Refresh variables after the treatment.
    $this->refreshVariables();

    // Disable all other rankings.
    $node_ranks = array('sticky', 'promote', 'recent', 'comments', 'views');
    foreach ($node_ranks as $node_rank) {
      variable_set('node_rank_' . $node_rank, 0);
    }
    $set = node_search_execute('rocks');

    // Test the ranking of each tag.
    foreach ($sorted_tags as $tag_rank => $tag) {
      // Assert the results.
      if ($tag == 'notag') {
        $this->assertEqual($set[$tag_rank]['node']->nid, $nodes[$tag]->nid, 'Search tag ranking for plain text order.');
      } else {
        $this->assertEqual($set[$tag_rank]['node']->nid, $nodes[$tag]->nid, 'Search tag ranking for "&lt;' . $sorted_tags[$tag_rank] . '&gt;" order.');
      }
    }

    // Test tags with the same weight against the sorted tags.
    $unsorted_tags = array('u', 'b', 'i', 'strong', 'em');
    foreach ($unsorted_tags as $tag) {
      $settings['body'] = array(LANGUAGE_NONE => array(array('value' => "<$tag>Drupal Rocks</$tag>", 'format' => 'full_html')));
      $node = $this->drupalCreateNode($settings);

      // Update the search index.
      module_invoke_all('update_index');
      search_update_totals();

      // Refresh variables after the treatment.
      $this->refreshVariables();

      $set = node_search_execute('rocks');

      // Ranking should always be second to last.
      $set = array_slice($set, -2, 1);

      // Assert the results.
      $this->assertEqual($set[0]['node']->nid, $node->nid, 'Search tag ranking for "&lt;' . $tag . '&gt;" order.');

      // Delete node so it doesn't show up in subsequent search results.
      node_delete($node->nid);
    }
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
