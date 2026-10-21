# SearchAdvancedSearchForm::setUp()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 327–344 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L327-L344)
- **Class:** [SearchAdvancedSearchForm](../SearchAdvancedSearchForm.md)
- **Module/theme:** search

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('search');
    // Create and login user.
    $test_user = $this->drupalCreateUser(array('access content', 'search content', 'use advanced search', 'administer nodes'));
    $this->drupalLogin($test_user);

    // Create initial node.
    $node = $this->drupalCreateNode();
    $this->node = $this->drupalCreateNode();

    // First update the index. This does the initial processing.
    node_update_index();

    // Then, run the shutdown function. Testing is a unique case where indexing
    // and searching has to happen in the same request, so running the shutdown
    // function manually is needed to finish the indexing process.
    search_update_totals();
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
