# search_node_tags_query_alter()

- **Type:** Function
- **File:** [`modules/search/tests/search_node_tags.module`](_file.md), lines 12–16 · [local source](../../../../../source/modules/search/tests/search_node_tags.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/tests/search_node_tags.module#L12-L16)
- **Module/theme:** search_node_tags
- **Implements:** [hook_query_alter()](../../../system/system.api.php/hook_query_alter.md)

## Signature

```php
function search_node_tags_query_alter(QueryAlterableInterface $query)
```

## Documentation

```text
 Implements hook_query_alter().
```

## Code

```php
function search_node_tags_query_alter(QueryAlterableInterface $query) {
  if ($query->hasTag('search_node')) {
    variable_set('search_node_tags_test_query_tag', TRUE);
  }
}
```

---
_Drupal 7.103 · [modules/search/tests/search_node_tags.module](https://github.com/drupal/drupal/blob/7.103/modules/search/tests/search_node_tags.module) · Licensed GPL-2.0-or-later (see LICENSE)._
