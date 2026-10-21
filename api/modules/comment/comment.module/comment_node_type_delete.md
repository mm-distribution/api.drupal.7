# comment_node_type_delete()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 343–357 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L343-L357)
- **Module/theme:** comment
- **Implements:** [hook_node_type_delete()](../../node/node.api.php/hook_node_type_delete.md)

## Signature

```php
function comment_node_type_delete($info)
```

## Documentation

```text
Implements hook_node_type_delete().
```

## Code

```php
function comment_node_type_delete($info) {
  field_attach_delete_bundle('comment', 'comment_node_' . $info->type);
  $settings = array(
    'comment',
    'comment_default_mode',
    'comment_default_per_page',
    'comment_anonymous',
    'comment_subject_field',
    'comment_preview',
    'comment_form_location',
  );
  foreach ($settings as $setting) {
    variable_del($setting . '_' . $info->type);
  }
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
