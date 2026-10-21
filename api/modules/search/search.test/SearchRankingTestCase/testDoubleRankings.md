# SearchRankingTestCase::testDoubleRankings()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 557–589 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L557-L589)
- **Class:** [SearchRankingTestCase](../SearchRankingTestCase.md)
- **Module/theme:** search

## Signature

```php
function testDoubleRankings()
```

## Documentation

```text
Verifies that if we combine two rankings, search still works.

See issue http://drupal.org/node/771596
```

## Code

```php
  function testDoubleRankings() {
    // Login with sufficient privileges.
    $this->drupalLogin($this->drupalCreateUser(array('skip comment approval', 'create page content')));

    // See testRankings() above - build a node that will rank high for sticky.
    $settings = array(
      'type' => 'page',
      'title' => 'Drupal rocks',
      'body' => array(LANGUAGE_NONE => array(array('value' => "Drupal's search rocks"))),
      'sticky' => 1,
    );

    $node = $this->drupalCreateNode($settings);

    // Update the search index.
    module_invoke_all('update_index');
    search_update_totals();

    // Refresh variables after the treatment.
    $this->refreshVariables();

    // Set up for ranking sticky and lots of comments; make sure others are
    // disabled.
    $node_ranks = array('sticky', 'promote', 'relevance', 'recent', 'comments', 'views');
    foreach ($node_ranks as $var) {
      $value = ($var == 'sticky' || $var == 'comments') ? 10 : 0;
      variable_set('node_rank_' . $var, $value);
    }

    // Do the search and assert the results.
    $set = node_search_execute('rocks');
    $this->assertEqual($set[0]['node']->nid, $node->nid, 'Search double ranking order.');
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
