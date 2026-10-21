# file_field_formatter_info()

- **Type:** Function
- **File:** [`modules/file/file.field.inc`](_file.md), lines 401–416 · [local source](../../../../source/modules/file/file.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc#L401-L416)
- **Module/theme:** file
- **Implements:** [hook_field_formatter_info()](../../field/field.api.php/hook_field_formatter_info.md)

## Signature

```php
function file_field_formatter_info()
```

## Documentation

```text
Implements hook_field_formatter_info().
```

## Code

```php
function file_field_formatter_info() {
  return array(
    'file_default' => array(
      'label' => t('Generic file'),
      'field types' => array('file'),
    ),
    'file_table' => array(
      'label' => t('Table of files'),
      'field types' => array('file'),
    ),
    'file_url_plain' => array(
      'label' => t('URL to file'),
      'field types' => array('file'),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/file/file.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
