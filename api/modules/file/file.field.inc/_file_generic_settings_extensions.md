# _file_generic_settings_extensions()

- **Type:** Function
- **File:** [`modules/file/file.field.inc`](_file.md), lines 141–153 · [local source](../../../../source/modules/file/file.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc#L141-L153)
- **Module/theme:** file

## Signature

```php
function _file_generic_settings_extensions($element, &$form_state)
```

## Documentation

```text
Element validate callback for the allowed file extensions field.

This doubles as a convenience clean-up function and a validation routine.
Commas are allowed by the end-user, but ultimately the value will be stored
as a space-separated list for compatibility with file_validate_extensions().
```

## Code

```php
function _file_generic_settings_extensions($element, &$form_state) {
  if (!empty($element['#value'])) {
    $extensions = preg_replace('/([, ]+\.?)/', ' ', trim(strtolower($element['#value'])));
    $extensions = array_filter(explode(' ', $extensions));
    $extensions = implode(' ', array_unique($extensions));
    if (!preg_match('/^([a-z0-9]+([.][a-z0-9])* ?)+$/', $extensions)) {
      form_error($element, t('The list of allowed extensions is not valid, be sure to exclude leading dots and to separate extensions with a comma or space.'));
    }
    else {
      form_set_value($element, $extensions, $form_state);
    }
  }
}
```

---
_Drupal 7.103 · [modules/file/file.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
