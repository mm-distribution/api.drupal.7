# tracker_node_update()

- **Type:** Function
- **File:** [`modules/tracker/tracker.module`](_file.md), lines 184–186 · [local source](../../../../source/modules/tracker/tracker.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.module#L184-L186)
- **Module/theme:** tracker
- **Implements:** [hook_node_update()](../../node/node.api.php/hook_node_update.md)

## Signature

```php
function tracker_node_update($node, $arg = 0)
```

## Documentation

```text
Implements hook_node_update().

Adds tracking information for this node since it's been updated.
```

## Code

```php
function tracker_node_update($node, $arg = 0) {
  _tracker_add($node->nid, $node->uid, $node->changed);
}
```

---
_Drupal 7.103 · [modules/tracker/tracker.module](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.module) · Licensed GPL-2.0-or-later (see LICENSE)._
