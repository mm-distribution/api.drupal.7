# _field_info_prepare_extra_fields()

- **Type:** Function
- **File:** [`modules/field/field.info.inc`](_file.md), lines 297–300 · [local source](../../../../source/modules/field/field.info.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc#L297-L300)
- **Module/theme:** field
- **Topics:** [field_info](../../../topics/field_info.md)

## Signature

```php
function _field_info_prepare_extra_fields($extra_fields, $entity_type, $bundle)
```

## Documentation

```text
Prepares 'extra fields' for the current run-time context.

The functionality has moved to the FieldInfo class. This function is kept as
a backwards-compatibility layer. See http://drupal.org/node/1915646.

@see FieldInfo::prepareExtraFields()
```

## Code

```php
function _field_info_prepare_extra_fields($extra_fields, $entity_type, $bundle) {
  $cache = _field_info_field_cache();
  return $cache->prepareExtraFields($extra_fields, $entity_type, $bundle);
}
```

---
_Drupal 7.103 · [modules/field/field.info.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
