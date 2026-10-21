# node_unpromote_action()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 3951–3954 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L3951-L3954)
- **Module/theme:** node
- **Topics:** [actions](../../../topics/actions.md)

## Signature

```php
function node_unpromote_action($node, $context = array())
```

## Documentation

```text
Sets the promote property of a node to 0.

@param $node
  A node object.
@param $context
  (optional) Array of additional information about what triggered the action.
  Not used for this action.

@ingroup actions
```

## Code

```php
function node_unpromote_action($node, $context = array()) {
  $node->promote = NODE_NOT_PROMOTED;
  watchdog('action', 'Removed @type %title from front page.', array('@type' => node_type_get_name($node), '%title' => $node->title));
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
