# file_field_widget_uri()

- **Type:** Function
- **File:** [`modules/file/file.field.inc`](_file.md), lines 584–591 · [local source](../../../../source/modules/file/file.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc#L584-L591)
- **Module/theme:** file

## Signature

```php
function file_field_widget_uri($field, $instance, $data = array())
```

## Documentation

```text
Determines the URI for a file field instance.

@param $field
  A field array.
@param $instance
  A field instance array.
@param $data
  An array of token objects to pass to token_replace().

@return
  A file directory URI with tokens replaced.

@see token_replace()
```

## Code

```php
function file_field_widget_uri($field, $instance, $data = array()) {
  $destination = trim($instance['settings']['file_directory'], '/');

  // Replace tokens.
  $destination = token_replace($destination, $data);

  return $field['settings']['uri_scheme'] . '://' . $destination;
}
```

---
_Drupal 7.103 · [modules/file/file.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
