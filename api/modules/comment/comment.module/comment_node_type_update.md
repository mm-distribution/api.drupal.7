# comment_node_type_update()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 334–338 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L334-L338)
- **Module/theme:** comment
- **Implements:** [hook_node_type_update()](../../node/node.api.php/hook_node_type_update.md)

## Signature

```php
function comment_node_type_update($info)
```

## Documentation

```text
Implements hook_node_type_update().
```

## Code

```php
function comment_node_type_update($info) {
  if (!empty($info->old_type) && $info->type != $info->old_type) {
    field_attach_rename_bundle('comment', 'comment_node_' . $info->old_type, 'comment_node_' . $info->type);
  }
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
