# file_field_widget_info()

- **Type:** Function
- **File:** [`modules/file/file.field.inc`](_file.md), lines 421–435 · [local source](../../../../source/modules/file/file.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc#L421-L435)
- **Module/theme:** file
- **Implements:** [hook_field_widget_info()](../../field/field.api.php/hook_field_widget_info.md)

## Signature

```php
function file_field_widget_info()
```

## Documentation

```text
Implements hook_field_widget_info().
```

## Code

```php
function file_field_widget_info() {
  return array(
    'file_generic' => array(
      'label' => t('File'),
      'field types' => array('file'),
      'settings' => array(
        'progress_indicator' => 'throbber',
      ),
      'behaviors' => array(
        'multiple values' => FIELD_BEHAVIOR_CUSTOM,
        'default value' => FIELD_BEHAVIOR_NONE,
      ),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/file/file.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
