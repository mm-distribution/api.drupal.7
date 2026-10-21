# image_field_delete_field()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 426–436 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L426-L436)
- **Module/theme:** image
- **Implements:** [hook_field_delete_field()](../../field/field.api.php/hook_field_delete_field.md)

## Signature

```php
function image_field_delete_field($field)
```

## Documentation

```text
Implements hook_field_delete_field().
```

## Code

```php
function image_field_delete_field($field) {
  if ($field['type'] != 'image') {
    return;
  }

  // The value of a managed_file element can be an array if #extended == TRUE.
  $fid = (is_array($field['settings']['default_image']) ? $field['settings']['default_image']['fid'] : $field['settings']['default_image']);
  if ($fid && ($file = file_load($fid))) {
    file_usage_delete($file, 'image', 'default_image', $field['id']);
  }
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
