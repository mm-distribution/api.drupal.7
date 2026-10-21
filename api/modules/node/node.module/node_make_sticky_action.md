# node_make_sticky_action()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 3903–3906 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L3903-L3906)
- **Module/theme:** node
- **Topics:** [actions](../../../topics/actions.md)

## Signature

```php
function node_make_sticky_action($node, $context = array())
```

## Documentation

```text
Sets the sticky-at-top-of-list property of a node to 1.

@param $node
  A node object.
@param $context
  (optional) Array of additional information about what triggered the action.
  Not used for this action.

@ingroup actions
```

## Code

```php
function node_make_sticky_action($node, $context = array()) {
  $node->sticky = NODE_STICKY;
  watchdog('action', 'Set @type %title to sticky.', array('@type' => node_type_get_name($node), '%title' => $node->title));
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
