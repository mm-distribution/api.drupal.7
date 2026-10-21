# node_publish_action()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 3871–3874 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L3871-L3874)
- **Module/theme:** node
- **Topics:** [actions](../../../topics/actions.md)

## Signature

```php
function node_publish_action($node, $context = array())
```

## Documentation

```text
Sets the status of a node to 1 (published).

@param $node
  A node object.
@param $context
  (optional) Array of additional information about what triggered the action.
  Not used for this action.

@ingroup actions
```

## Code

```php
function node_publish_action($node, $context = array()) {
  $node->status = NODE_PUBLISHED;
  watchdog('action', 'Set @type %title to published.', array('@type' => node_type_get_name($node), '%title' => $node->title));
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
