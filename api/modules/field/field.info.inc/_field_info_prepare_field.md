# _field_info_prepare_field()

- **Type:** Function
- **File:** [`modules/field/field.info.inc`](_file.md), lines 245–248 · [local source](../../../../source/modules/field/field.info.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc#L245-L248)
- **Module/theme:** field
- **Topics:** [field_info](../../../topics/field_info.md)

## Signature

```php
function _field_info_prepare_field($field)
```

## Documentation

```text
Prepares a field definition for the current run-time context.

The functionality has moved to the FieldInfo class. This function is kept as
a backwards-compatibility layer. See http://drupal.org/node/1915646.

@see FieldInfo::prepareField()
```

## Code

```php
function _field_info_prepare_field($field) {
  $cache = _field_info_field_cache();
  return $cache->prepareField($field);
}
```

---
_Drupal 7.103 · [modules/field/field.info.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
