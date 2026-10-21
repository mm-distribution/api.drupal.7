# comment_node_type_insert()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 327–329 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L327-L329)
- **Module/theme:** comment
- **Implements:** [hook_node_type_insert()](../../node/node.api.php/hook_node_type_insert.md)

## Signature

```php
function comment_node_type_insert($info)
```

## Documentation

```text
Implements hook_node_type_insert().

Creates a comment body field for a node type created while the comment module
is enabled. For node types created before the comment module is enabled,
hook_modules_enabled() serves to create the body fields.

@see comment_modules_enabled()
```

## Code

```php
function comment_node_type_insert($info) {
  _comment_body_field_create($info);
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
