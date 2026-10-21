# hook_node_revision_delete()

- **Type:** Hook (documentation function)
- **File:** [`modules/node/node.api.php`](_file.md), lines 493–497 · [local source](../../../../source/modules/node/node.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php#L493-L497)
- **Module/theme:** node
- **Topics:** [hooks](../../../topics/hooks.md), [node_api_hooks](../../../topics/node_api_hooks.md)

## Signature

```php
function hook_node_revision_delete($node)
```

## Documentation

```text
Respond to deletion of a node revision.

This hook is invoked from node_revision_delete() after the revision has been
removed from the node_revision table, and before
field_attach_delete_revision() is called.

@param $node
  The node revision (node object) that is being deleted.

@ingroup node_api_hooks
```

## Code

```php
function hook_node_revision_delete($node) {
  db_delete('mytable')
    ->condition('vid', $node->vid)
    ->execute();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_node_revision_delete()".

_None found._

---
_Drupal 7.103 · [modules/node/node.api.php](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
