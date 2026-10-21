# _file_generic_settings_file_directory_validate()

- **Type:** Function
- **File:** [`modules/file/file.field.inc`](_file.md), lines 161–165 · [local source](../../../../source/modules/file/file.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc#L161-L165)
- **Module/theme:** file

## Signature

```php
function _file_generic_settings_file_directory_validate($element, &$form_state)
```

## Documentation

```text
Element validate callback for the file destination field.

Remove slashes from the beginning and end of the destination value and ensure
that the file directory path is not included at the beginning of the value.
```

## Code

```php
function _file_generic_settings_file_directory_validate($element, &$form_state) {
  // Strip slashes from the beginning and end of $widget['file_directory'].
  $value = trim($element['#value'], '\\/');
  form_set_value($element, $value, $form_state);
}
```

---
_Drupal 7.103 · [modules/file/file.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
