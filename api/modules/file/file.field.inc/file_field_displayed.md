# file_field_displayed()

- **Type:** Function
- **File:** [`modules/file/file.field.inc`](_file.md), lines 391–396 · [local source](../../../../source/modules/file/file.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc#L391-L396)
- **Module/theme:** file

## Signature

```php
function file_field_displayed($item, $field)
```

## Documentation

```text
Determines whether a file should be displayed when outputting field content.

@param $item
  A field item array.
@param $field
  A field array.

@return
  Boolean TRUE if the file will be displayed, FALSE if the file is hidden.
```

## Code

```php
function file_field_displayed($item, $field) {
  if (!empty($field['settings']['display_field'])) {
    return (bool) $item['display'];
  }
  return TRUE;
}
```

---
_Drupal 7.103 · [modules/file/file.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
