# search_node_update()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 809–813 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L809-L813)
- **Module/theme:** search
- **Implements:** [hook_node_update()](../../node/node.api.php/hook_node_update.md)

## Signature

```php
function search_node_update($node)
```

## Documentation

```text
Implements hook_node_update().
```

## Code

```php
function search_node_update($node) {
  // Reindex the node when it is updated. The node is automatically indexed
  // when it is added, simply by being added to the node table.
  search_touch_node($node->nid);
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
