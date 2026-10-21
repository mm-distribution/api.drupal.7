# hook_update()

- **Type:** Hook (documentation function)
- **File:** [`modules/node/node.api.php`](_file.md), lines 1236–1241 · [local source](../../../../source/modules/node/node.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php#L1236-L1241)
- **Module/theme:** node
- **Topics:** [hooks](../../../topics/hooks.md), [node_api_hooks](../../../topics/node_api_hooks.md)

## Signature

```php
function hook_update($node)
```

## Documentation

```text
Respond to updates to a node.

This is a node-type-specific hook, which is invoked only for the node type
being affected. See
@link node_api_hooks Node API hooks @endlink for more information.

Use hook_node_update() to respond to node update of all node types.

This hook is invoked from node_save() after the node is updated in the
node table in the database, before field_attach_update() is called, and
before hook_node_update() is invoked.

@param $node
  The node that is being updated.

@ingroup node_api_hooks
```

## Code

```php
function hook_update($node) {
  db_update('mytable')
    ->fields(array('extra' => $node->extra))
    ->condition('nid', $node->nid)
    ->execute();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_update()".

- [poll_update()](../../poll/poll.module/poll_update.md) — `modules/poll/poll.module`

---
_Drupal 7.103 · [modules/node/node.api.php](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
