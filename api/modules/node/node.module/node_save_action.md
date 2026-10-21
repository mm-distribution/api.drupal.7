# node_save_action()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 3964–3967 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L3964-L3967)
- **Module/theme:** node
- **Topics:** [actions](../../../topics/actions.md)

## Signature

```php
function node_save_action($node)
```

## Documentation

```text
Saves a node.

@param $node
  The node to be saved.

@ingroup actions
```

## Code

```php
function node_save_action($node) {
  node_save($node);
  watchdog('action', 'Saved @type %title', array('@type' => node_type_get_name($node), '%title' => $node->title));
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
