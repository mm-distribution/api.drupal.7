# hook_node_type_update()

- **Type:** Hook (documentation function)
- **File:** [`modules/node/node.api.php`](_file.md), lines 1016–1022 · [local source](../../../../source/modules/node/node.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php#L1016-L1022)
- **Module/theme:** node
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_node_type_update($info)
```

## Documentation

```text
Respond to node type updates.

This hook is invoked from node_type_save() after the node type is updated in
the database.

@param $info
  The node type object that is being updated.
```

## Code

```php
function hook_node_type_update($info) {
  if (!empty($info->old_type) && $info->old_type != $info->type) {
    $setting = variable_get('comment_' . $info->old_type, COMMENT_NODE_OPEN);
    variable_del('comment_' . $info->old_type);
    variable_set('comment_' . $info->type, $setting);
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_node_type_update()".

- [book_node_type_update()](../../book/book.module/book_node_type_update.md) — `modules/book/book.module`
- [comment_node_type_update()](../../comment/comment.module/comment_node_type_update.md) — `modules/comment/comment.module`
- [node_node_type_update()](../content_types.inc/node_node_type_update.md) — `modules/node/content_types.inc`

---
_Drupal 7.103 · [modules/node/node.api.php](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
