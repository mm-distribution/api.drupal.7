# tracker_node_insert()

- **Type:** Function
- **File:** [`modules/tracker/tracker.module`](_file.md), lines 175–177 · [local source](../../../../source/modules/tracker/tracker.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.module#L175-L177)
- **Module/theme:** tracker
- **Implements:** [hook_node_insert()](../../node/node.api.php/hook_node_insert.md)

## Signature

```php
function tracker_node_insert($node, $arg = 0)
```

## Documentation

```text
Implements hook_node_insert().

Adds new tracking information for this node since it's new.
```

## Code

```php
function tracker_node_insert($node, $arg = 0) {
  _tracker_add($node->nid, $node->uid, $node->changed);
}
```

---
_Drupal 7.103 · [modules/tracker/tracker.module](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.module) · Licensed GPL-2.0-or-later (see LICENSE)._
