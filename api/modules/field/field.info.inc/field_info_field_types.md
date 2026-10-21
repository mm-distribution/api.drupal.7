# field_info_field_types()

- **Type:** Function
- **File:** [`modules/field/field.info.inc`](_file.md), lines 333–344 · [local source](../../../../source/modules/field/field.info.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc#L333-L344)
- **Module/theme:** field
- **Topics:** [field_info](../../../topics/field_info.md)

## Signature

```php
function field_info_field_types($field_type = NULL)
```

## Documentation

```text
Returns information about field types from hook_field_info().

@param $field_type
  (optional) A field type name. If omitted, all field types will be
  returned.

@return
  Either a field type description, as provided by hook_field_info(), or an
  array of all existing field types, keyed by field type name.
```

## Code

```php
function field_info_field_types($field_type = NULL) {
  $info = _field_info_collate_types();
  $field_types = $info['field types'];
  if ($field_type) {
    if (isset($field_types[$field_type])) {
      return $field_types[$field_type];
    }
  }
  else {
    return $field_types;
  }
}
```

---
_Drupal 7.103 · [modules/field/field.info.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
