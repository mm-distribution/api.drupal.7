# SearchRankingTestCase::testRankings()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 398–468 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L398-L468)
- **Class:** [SearchRankingTestCase](../SearchRankingTestCase.md)
- **Module/theme:** search

## Signature

```php
function testRankings()
```

## Documentation

_No docblock in source._

## Code

```php
  function testRankings() {
    // Login with sufficient privileges.
    $this->drupalLogin($this->drupalCreateUser(array('skip comment approval', 'create page content')));

    // Build a list of the rankings to test.
    $node_ranks = array('sticky', 'promote', 'relevance', 'recent', 'comments', 'views');

    // Create nodes for testing.
    foreach ($node_ranks as $node_rank) {
      $settings = array(
        'type' => 'page',
        'title' => 'Drupal rocks',
        'body' => array(LANGUAGE_NONE => array(array('value' => "Drupal's search rocks"))),
      );
      foreach (array(0, 1) as $num) {
        if ($num == 1) {
          switch ($node_rank) {
            case 'sticky':
            case 'promote':
              $settings[$node_rank] = 1;
              break;
            case 'relevance':
              $settings['body'][LANGUAGE_NONE][0]['value'] .= " really rocks";
              break;
            case 'recent':
              $settings['created'] = REQUEST_TIME + 3600;
              break;
            case 'comments':
              $settings['comment'] = 2;
              break;
          }
        }
        $nodes[$node_rank][$num] = $this->drupalCreateNode($settings);
      }
    }

    // Update the search index.
    module_invoke_all('update_index');
    search_update_totals();

    // Refresh variables after the treatment.
    $this->refreshVariables();

    // Add a comment to one of the nodes.
    $edit = array();
    $edit['subject'] = 'my comment title';
    $edit['comment_body[' . LANGUAGE_NONE . '][0][value]'] = 'some random comment';
    $this->drupalGet('comment/reply/' . $nodes['comments'][1]->nid);
    $this->drupalPost(NULL, $edit, t('Preview'));
    $this->drupalPost(NULL, $edit, t('Save'));

    // Enable counting of statistics.
    variable_set('statistics_count_content_views', 1);

    // Then View one of the nodes a bunch of times.
    for ($i = 0; $i < 5; $i ++) {
      $this->drupalGet('node/' . $nodes['views'][1]->nid);
    }

    // Test each of the possible rankings.
    foreach ($node_ranks as $node_rank) {
      // Disable all relevancy rankings except the one we are testing.
      foreach ($node_ranks as $var) {
        variable_set('node_rank_' . $var, $var == $node_rank ? 10 : 0);
      }

      // Do the search and assert the results.
      $set = node_search_execute('rocks');
      $this->assertEqual($set[0]['node']->nid, $nodes[$node_rank][1]->nid, 'Search ranking "' . $node_rank . '" order.');
    }
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
