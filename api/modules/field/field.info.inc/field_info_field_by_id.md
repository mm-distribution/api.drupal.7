# field_info_field_by_id()

- **Type:** Function
- **File:** [`modules/field/field.info.inc`](_file.md), lines 541–544 · [local source](../../../../source/modules/field/field.info.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc#L541-L544)
- **Module/theme:** field
- **Topics:** [field_info](../../../topics/field_info.md)

## Signature

```php
function field_info_field_by_id($field_id)
```

## Documentation

```text
Returns data about an individual field, given a field ID.

@param $field_id
  The id of the field to retrieve. $field_id can refer to a
  deleted field, but not an inactive one.

@return
  The field array, as returned by field_read_fields(), with an
  additional element 'bundles', whose value is an array of all the bundles
  this field belongs to.

@see field_info_field()
```

## Code

```php
function field_info_field_by_id($field_id) {
  $cache = _field_info_field_cache();
  return $cache->getFieldById($field_id);
}
```

---
_Drupal 7.103 · [modules/field/field.info.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
