# image_field_update_instance()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 501–540 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L501-L540)
- **Module/theme:** image
- **Implements:** [hook_field_update_instance()](../../field/field.api.php/hook_field_update_instance.md)

## Signature

```php
function image_field_update_instance($instance, $prior_instance)
```

## Documentation

```text
Implements hook_field_update_instance().
```

## Code

```php
function image_field_update_instance($instance, $prior_instance) {
  // Only act on image fields.
  $field = field_read_field($instance['field_name']);
  if ($field['type'] != 'image') {
    return;
  }

  // The value of a managed_file element can be an array if the #extended
  // property is set to TRUE.
  $fid_new = $instance['settings']['default_image'];
  if (is_array($fid_new)) {
    $fid_new = $fid_new['fid'];
  }
  $fid_old = $prior_instance['settings']['default_image'];
  if (is_array($fid_old)) {
    $fid_old = $fid_old['fid'];
  }

  // If the old and new files do not match, update the default accordingly.
  $file_new = $fid_new ? file_load($fid_new) : FALSE;
  if ($fid_new != $fid_old) {
    // Save the new file, if present.
    if ($file_new) {
      $file_new->status = FILE_STATUS_PERMANENT;
      file_save($file_new);
      file_usage_add($file_new, 'image', 'default_image', $instance['id']);
    }
    // Delete the old file, if present.
    if ($fid_old && ($file_old = file_load($fid_old))) {
      file_usage_delete($file_old, 'image', 'default_image', $instance['id']);
    }
  }

  // If the upload destination changed, then move the file.
  if ($file_new && (file_uri_scheme($file_new->uri) != $field['settings']['uri_scheme'])) {
    $directory = $field['settings']['uri_scheme'] . '://default_images/';
    file_prepare_directory($directory, FILE_CREATE_DIRECTORY);
    file_move($file_new, $directory . $file_new->filename);
  }
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
