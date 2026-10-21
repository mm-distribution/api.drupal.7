# field_read_field()

- **Type:** Function
- **File:** [`modules/field/field.crud.inc`](_file.md), lines 331–334 · [local source](../../../../source/modules/field/field.crud.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.crud.inc#L331-L334)
- **Module/theme:** field
- **Topics:** [field_crud](../../../topics/field_crud.md)

## Signature

```php
function field_read_field($field_name, $include_additional = array())
```

## Documentation

```text
Reads a single field record directly from the database.

Generally, you should use the field_info_field() instead.

This function will not return deleted fields. Use
field_read_fields() instead for this purpose.

@param $field_name
  The field name to read.
@param array $include_additional
  The default behavior of this function is to not return a field that
  is inactive. Setting
  $include_additional['include_inactive'] to TRUE will override this
  behavior.
@return
  A field definition array, or FALSE.
```

## Code

```php
function field_read_field($field_name, $include_additional = array()) {
  $fields = field_read_fields(array('field_name' => $field_name), $include_additional);
  return $fields ? current($fields) : FALSE;
}
```

---
_Drupal 7.103 · [modules/field/field.crud.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.crud.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
