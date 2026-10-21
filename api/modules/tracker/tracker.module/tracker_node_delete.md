# tracker_node_delete()

- **Type:** Function
- **File:** [`modules/tracker/tracker.module`](_file.md), lines 193–200 · [local source](../../../../source/modules/tracker/tracker.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.module#L193-L200)
- **Module/theme:** tracker
- **Implements:** [hook_node_delete()](../../node/node.api.php/hook_node_delete.md)

## Signature

```php
function tracker_node_delete($node, $arg = 0)
```

## Documentation

```text
Implements hook_node_delete().

Deletes tracking information for a node.
```

## Code

```php
function tracker_node_delete($node, $arg = 0) {
  db_delete('tracker_node')
    ->condition('nid', $node->nid)
    ->execute();
  db_delete('tracker_user')
    ->condition('nid', $node->nid)
    ->execute();
}
```

---
_Drupal 7.103 · [modules/tracker/tracker.module](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.module) · Licensed GPL-2.0-or-later (see LICENSE)._
