# image_field_delete_instance()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 478–496 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L478-L496)
- **Module/theme:** image
- **Implements:** [hook_field_delete_instance()](../../field/field.api.php/hook_field_delete_instance.md)

## Signature

```php
function image_field_delete_instance($instance)
```

## Documentation

```text
Implements hook_field_delete_instance().
```

## Code

```php
function image_field_delete_instance($instance) {
  // Only act on image fields.
  $field = field_read_field($instance['field_name']);
  if ($field['type'] != 'image') {
    return;
  }

  // The value of a managed_file element can be an array if the #extended
  // property is set to TRUE.
  $fid = $instance['settings']['default_image'];
  if (is_array($fid)) {
    $fid = $fid['fid'];
  }

  // Remove the default image when the instance is deleted.
  if ($fid && ($file = file_load($fid))) {
    file_usage_delete($file, 'image', 'default_image', $instance['id']);
  }
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
