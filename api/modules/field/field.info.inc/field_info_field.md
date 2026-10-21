# field_info_field()

- **Type:** Function
- **File:** [`modules/field/field.info.inc`](_file.md), lines 522–525 · [local source](../../../../source/modules/field/field.info.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc#L522-L525)
- **Module/theme:** field
- **Topics:** [field_info](../../../topics/field_info.md)

## Signature

```php
function field_info_field($field_name)
```

## Documentation

```text
Returns data about an individual field, given a field name.

@param $field_name
  The name of the field to retrieve. $field_name can only refer to a
  non-deleted, active field. For deleted fields, use
  field_info_field_by_id(). To retrieve information about inactive fields,
  use field_read_fields().

@return
  The field array, as returned by field_read_fields(), with an
  additional element 'bundles', whose value is an array of all the bundles
  this field belongs to keyed by entity type. NULL if the field was not
  found.

@see field_info_field_by_id()
```

## Code

```php
function field_info_field($field_name) {
  $cache = _field_info_field_cache();
  return $cache->getField($field_name);
}
```

---
_Drupal 7.103 · [modules/field/field.info.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
