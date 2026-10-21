# file_field_info()

- **Type:** Function
- **File:** [`modules/file/file.field.inc`](_file.md), lines 11–31 · [local source](../../../../source/modules/file/file.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc#L11-L31)
- **Module/theme:** file
- **Implements:** [hook_field_info()](../../field/field.api.php/hook_field_info.md)

## Signature

```php
function file_field_info()
```

## Documentation

```text
Implements hook_field_info().
```

## Code

```php
function file_field_info() {
  return array(
    'file' => array(
      'label' => t('File'),
      'description' => t('This field stores the ID of a file as an integer value.'),
      'settings' => array(
        'display_field' => 0,
        'display_default' => 0,
        'uri_scheme' => variable_get('file_default_scheme', 'public'),
      ),
      'instance_settings' => array(
        'file_extensions' => 'txt',
        'file_directory' => '[date:custom:Y]-[date:custom:m]',
        'max_filesize' => '',
        'description_field' => 0,
      ),
      'default_widget' => 'file_generic',
      'default_formatter' => 'file_default',
    ),
  );
}
```

---
_Drupal 7.103 · [modules/file/file.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
