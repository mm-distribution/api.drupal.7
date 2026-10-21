# image_field_update_field()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 441–473 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L441-L473)
- **Module/theme:** image
- **Implements:** [hook_field_update_field()](../../field/field.api.php/hook_field_update_field.md)

## Signature

```php
function image_field_update_field($field, $prior_field, $has_data)
```

## Documentation

```text
Implements hook_field_update_field().
```

## Code

```php
function image_field_update_field($field, $prior_field, $has_data) {
  if ($field['type'] != 'image') {
    return;
  }

  // The value of a managed_file element can be an array if #extended == TRUE.
  $fid_new = (is_array($field['settings']['default_image']) ? $field['settings']['default_image']['fid'] : $field['settings']['default_image']);
  $fid_old = (is_array($prior_field['settings']['default_image']) ? $prior_field['settings']['default_image']['fid'] : $prior_field['settings']['default_image']);

  $file_new = $fid_new ? file_load($fid_new) : FALSE;

  if ($fid_new != $fid_old) {

    // Is there a new file?
    if ($file_new) {
      $file_new->status = FILE_STATUS_PERMANENT;
      file_save($file_new);
      file_usage_add($file_new, 'image', 'default_image', $field['id']);
    }

    // Is there an old file?
    if ($fid_old && ($file_old = file_load($fid_old))) {
      file_usage_delete($file_old, 'image', 'default_image', $field['id']);
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
