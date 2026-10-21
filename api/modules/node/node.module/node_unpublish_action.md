# node_unpublish_action()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 3887–3890 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L3887-L3890)
- **Module/theme:** node
- **Topics:** [actions](../../../topics/actions.md)

## Signature

```php
function node_unpublish_action($node, $context = array())
```

## Documentation

```text
Sets the status of a node to 0 (unpublished).

@param $node
  A node object.
@param $context
  (optional) Array of additional information about what triggered the action.
  Not used for this action.

@ingroup actions
```

## Code

```php
function node_unpublish_action($node, $context = array()) {
  $node->status = NODE_NOT_PUBLISHED;
  watchdog('action', 'Set @type %title to unpublished.', array('@type' => node_type_get_name($node), '%title' => $node->title));
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
