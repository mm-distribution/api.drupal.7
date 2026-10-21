# SearchNodeTagTest::testNodeSearchQueryTags()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 2124–2136 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L2124-L2136)
- **Class:** [SearchNodeTagTest](../SearchNodeTagTest.md)
- **Module/theme:** search

## Signature

```php
function testNodeSearchQueryTags()
```

## Documentation

```text
Tests that the correct tags are available and hooks invoked.
```

## Code

```php
  function testNodeSearchQueryTags() {
    $this->drupalCreateNode(array('body' => array(LANGUAGE_NONE => array(array('value' => 'testing testing testing.')))));

    // Update the search index.
    module_invoke_all('update_index');
    search_update_totals();

    $edit = array('keys' => 'testing');
    $this->drupalPost('search/node', $edit, t('Search'));

    $this->assertTrue(variable_get('search_node_tags_test_query_tag', FALSE), 'hook_query_alter() was invoked and the query contained the "search_node" tag.');
    $this->assertTrue(variable_get('search_node_tags_test_query_tag_hook', FALSE), 'hook_query_search_node_alter() was invoked.');
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
