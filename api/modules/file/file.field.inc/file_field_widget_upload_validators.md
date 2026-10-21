# file_field_widget_upload_validators()

- **Type:** Function
- **File:** [`modules/file/file.field.inc`](_file.md), lines 549–567 · [local source](../../../../source/modules/file/file.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc#L549-L567)
- **Module/theme:** file

## Signature

```php
function file_field_widget_upload_validators($field, $instance)
```

## Documentation

```text
Retrieves the upload validators for a file field.

@param $field
  A field array.

@return
  An array suitable for passing to file_save_upload() or the file field
  element's '#upload_validators' property.
```

## Code

```php
function file_field_widget_upload_validators($field, $instance) {
  // Cap the upload size according to the PHP limit.
  $max_filesize = parse_size(file_upload_max_size());
  if (!empty($instance['settings']['max_filesize']) && parse_size($instance['settings']['max_filesize']) < $max_filesize) {
    $max_filesize = parse_size($instance['settings']['max_filesize']);
  }

  $validators = array();

  // There is always a file size limit due to the PHP server limit.
  $validators['file_validate_size'] = array($max_filesize);

  // Add the extension check if necessary.
  if (!empty($instance['settings']['file_extensions'])) {
    $validators['file_validate_extensions'] = array($instance['settings']['file_extensions']);
  }

  return $validators;
}
```

---
_Drupal 7.103 · [modules/file/file.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
