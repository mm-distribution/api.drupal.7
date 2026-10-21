# search_node_tags_query_search_node_alter()

- **Type:** Function
- **File:** [`modules/search/tests/search_node_tags.module`](_file.md), lines 21–23 · [local source](../../../../../source/modules/search/tests/search_node_tags.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/tests/search_node_tags.module#L21-L23)
- **Module/theme:** search_node_tags
- **Implements:** [hook_query_TAG_alter()](../../../system/system.api.php/hook_query_TAG_alter.md)

## Signature

```php
function search_node_tags_query_search_node_alter(QueryAlterableInterface $query)
```

## Documentation

```text
 Implements hook_query_TAG_alter().
```

## Code

```php
function search_node_tags_query_search_node_alter(QueryAlterableInterface $query) {
  variable_set('search_node_tags_test_query_tag_hook', TRUE);
}
```

---
_Drupal 7.103 · [modules/search/tests/search_node_tags.module](https://github.com/drupal/drupal/blob/7.103/modules/search/tests/search_node_tags.module) · Licensed GPL-2.0-or-later (see LICENSE)._
