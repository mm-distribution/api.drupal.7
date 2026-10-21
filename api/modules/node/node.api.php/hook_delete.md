# hook_delete()

- **Type:** Hook (documentation function)
- **File:** [`modules/node/node.api.php`](_file.md), lines 1063–1067 · [local source](../../../../source/modules/node/node.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php#L1063-L1067)
- **Module/theme:** node
- **Topics:** [hooks](../../../topics/hooks.md), [node_api_hooks](../../../topics/node_api_hooks.md)

## Signature

```php
function hook_delete($node)
```

## Documentation

```text
Respond to node deletion.

This is a node-type-specific hook, which is invoked only for the node type
being affected. See
@link node_api_hooks Node API hooks @endlink for more information.

Use hook_node_delete() to respond to node deletion of all node types.

This hook is invoked from node_delete_multiple() before hook_node_delete()
is invoked and before field_attach_delete() is called.

Note that when this hook is invoked, the changes have not yet been written
to the database, because a database transaction is still in progress. The
transaction is not finalized until the delete operation is entirely
completed and node_delete_multiple() goes out of scope. You should not rely
on data in the database at this time as it is not updated yet. You should
also note that any write/update database queries executed from this hook are
also not committed immediately. Check node_delete_multiple() and
db_transaction() for more info.

@param $node
  The node that is being deleted.

@ingroup node_api_hooks
```

## Code

```php
function hook_delete($node) {
  db_delete('mytable')
    ->condition('nid', $node->nid)
    ->execute();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_delete()".

- [poll_delete()](../../poll/poll.module/poll_delete.md) — `modules/poll/poll.module`

---
_Drupal 7.103 · [modules/node/node.api.php](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
