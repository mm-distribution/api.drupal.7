# _field_info_prepare_instance()

- **Type:** Function
- **File:** [`modules/field/field.info.inc`](_file.md), lines 258–261 · [local source](../../../../source/modules/field/field.info.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc#L258-L261)
- **Module/theme:** field
- **Topics:** [field_info](../../../topics/field_info.md)

## Signature

```php
function _field_info_prepare_instance($instance, $field)
```

## Documentation

```text
Prepares an instance definition for the current run-time context.

The functionality has moved to the FieldInfo class. This function is kept as
a backwards-compatibility layer. See http://drupal.org/node/1915646.

@see FieldInfo::prepareInstance()
```

## Code

```php
function _field_info_prepare_instance($instance, $field) {
  $cache = _field_info_field_cache();
  return $cache->prepareInstance($instance, $field['type']);
}
```

---
_Drupal 7.103 · [modules/field/field.info.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
