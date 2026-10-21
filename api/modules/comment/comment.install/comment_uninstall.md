# comment_uninstall()

- **Type:** Function
- **File:** [`modules/comment/comment.install`](_file.md), lines 11–27 · [local source](../../../../source/modules/comment/comment.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.install#L11-L27)
- **Module/theme:** comment
- **Implements:** [hook_uninstall()](../../system/system.api.php/hook_uninstall.md)

## Signature

```php
function comment_uninstall()
```

## Documentation

```text
Implements hook_uninstall().
```

## Code

```php
function comment_uninstall() {
  // Remove variables.
  variable_del('comment_block_count');
  $node_types = array_keys(node_type_get_types());
  foreach ($node_types as $node_type) {
    field_attach_delete_bundle('comment', 'comment_node_' . $node_type);
    variable_del('comment_' . $node_type);
    variable_del('comment_anonymous_' . $node_type);
    variable_del('comment_controls_' . $node_type);
    variable_del('comment_default_mode_' . $node_type);
    variable_del('comment_default_order_' . $node_type);
    variable_del('comment_default_per_page_' . $node_type);
    variable_del('comment_form_location_' . $node_type);
    variable_del('comment_preview_' . $node_type);
    variable_del('comment_subject_field_' . $node_type);
  }
}
```

---
_Drupal 7.103 · [modules/comment/comment.install](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.install) · Licensed GPL-2.0-or-later (see LICENSE)._
