# field_info_field_by_ids()

- **Type:** Function
- **File:** [`modules/field/field.info.inc`](_file.md), lines 564–567 · [local source](../../../../source/modules/field/field.info.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc#L564-L567)
- **Module/theme:** field
- **Topics:** [field_info](../../../topics/field_info.md)

## Signature

```php
function field_info_field_by_ids()
```

## Documentation

```text
Returns the same data as field_info_field_by_id() for every field.

Use of this function should be avoided when possible, since it loads and
statically caches a potentially large array of information.

When iterating over the fields present in a given bundle after a call to
field_info_instances($entity_type, $bundle), it is recommended to use
field_info_field() on each individual field instead.

@return
  An array, each key is a field ID and the values are field arrays as
  returned by field_read_fields(), with an additional element 'bundles',
  whose value is an array of all the bundle this field belongs to.

@see field_info_field()
@see field_info_field_by_id()
```

## Code

```php
function field_info_field_by_ids() {
  $cache = _field_info_field_cache();
  return $cache->getFields();
}
```

---
_Drupal 7.103 · [modules/field/field.info.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
