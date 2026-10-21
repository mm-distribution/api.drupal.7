# _file_generic_settings_max_filesize()

- **Type:** Function
- **File:** [`modules/file/file.field.inc`](_file.md), lines 128–132 · [local source](../../../../source/modules/file/file.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc#L128-L132)
- **Module/theme:** file

## Signature

```php
function _file_generic_settings_max_filesize($element, &$form_state)
```

## Documentation

```text
Element validate callback for the maximum upload size field.

Ensure a size that can be parsed by parse_size() has been entered.
```

## Code

```php
function _file_generic_settings_max_filesize($element, &$form_state) {
  if (!empty($element['#value']) && !is_numeric(parse_size($element['#value']))) {
    form_error($element, t('The "!name" option must contain a valid value. You may either leave the text field empty or enter a string like "512" (bytes), "80 KB" (kilobytes) or "50 MB" (megabytes).', array('!name' => t($element['title']))));
  }
}
```

---
_Drupal 7.103 · [modules/file/file.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
