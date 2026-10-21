# _field_info_prepare_instance_display()

- **Type:** Function
- **File:** [`modules/field/field.info.inc`](_file.md), lines 271–274 · [local source](../../../../source/modules/field/field.info.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc#L271-L274)
- **Module/theme:** field
- **Topics:** [field_info](../../../topics/field_info.md)

## Signature

```php
function _field_info_prepare_instance_display($field, $display)
```

## Documentation

```text
Adapts display specifications to the current run-time context.

The functionality has moved to the FieldInfo class. This function is kept as
a backwards-compatibility layer. See http://drupal.org/node/1915646.

@see FieldInfo::prepareInstanceDisplay()
```

## Code

```php
function _field_info_prepare_instance_display($field, $display) {
  $cache = _field_info_field_cache();
  return $cache->prepareInstanceDisplay($display, $field['type']);
}
```

---
_Drupal 7.103 · [modules/field/field.info.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
