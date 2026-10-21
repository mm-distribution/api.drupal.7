# hook_node_type_insert()

- **Type:** Hook (documentation function)
- **File:** [`modules/node/node.api.php`](_file.md), lines 1003–1005 · [local source](../../../../source/modules/node/node.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php#L1003-L1005)
- **Module/theme:** node
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_node_type_insert($info)
```

## Documentation

```text
Respond to node type creation.

This hook is invoked from node_type_save() after the node type is added to
the database.

@param $info
  The node type object that is being created.
```

## Code

```php
function hook_node_type_insert($info) {
  drupal_set_message(t('You have just created a content type with a machine name %type.', array('%type' => $info->type)));
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_node_type_insert()".

- [comment_node_type_insert()](../../comment/comment.module/comment_node_type_insert.md) — `modules/comment/comment.module`
- [node_node_type_insert()](../content_types.inc/node_node_type_insert.md) — `modules/node/content_types.inc`

---
_Drupal 7.103 · [modules/node/node.api.php](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
