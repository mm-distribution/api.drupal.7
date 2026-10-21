# _file_field_get_description_from_element()

- **Type:** Function
- **File:** [`modules/file/file.field.inc`](_file.md), lines 739–750 · [local source](../../../../source/modules/file/file.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc#L739-L750)
- **Module/theme:** file

## Signature

```php
function _file_field_get_description_from_element($element)
```

## Documentation

```text
Retrieves the file description from a field field element.

This helper function is used by file_field_widget_process_multiple().

@param $element
  The element being processed.

@return
  A description of the file suitable for use in the administrative interface.
```

## Code

```php
function _file_field_get_description_from_element($element) {
  // Use the actual file description, if it's available.
  if (!empty($element['#default_value']['description'])) {
    return $element['#default_value']['description'];
  }
  // Otherwise, fall back to the filename.
  if (!empty($element['#default_value']['filename'])) {
    return $element['#default_value']['filename'];
  }
  // This is probably a newly uploaded file; no description is available.
  return FALSE;
}
```

---
_Drupal 7.103 · [modules/file/file.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
