# hook_node_type_delete()

- **Type:** Hook (documentation function)
- **File:** [`modules/node/node.api.php`](_file.md), lines 1033–1035 · [local source](../../../../source/modules/node/node.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php#L1033-L1035)
- **Module/theme:** node
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_node_type_delete($info)
```

## Documentation

```text
Respond to node type deletion.

This hook is invoked from node_type_delete() after the node type is removed
from the database.

@param $info
  The node type object that is being deleted.
```

## Code

```php
function hook_node_type_delete($info) {
  variable_del('comment_' . $info->type);
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_node_type_delete()".

- [comment_node_type_delete()](../../comment/comment.module/comment_node_type_delete.md) — `modules/comment/comment.module`

---
_Drupal 7.103 · [modules/node/node.api.php](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
