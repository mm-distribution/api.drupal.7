# field_info_instance_settings()

- **Type:** Function
- **File:** [`modules/field/field.info.inc`](_file.md), lines 761–764 · [local source](../../../../source/modules/field/field.info.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc#L761-L764)
- **Module/theme:** field
- **Topics:** [field_info](../../../topics/field_info.md)

## Signature

```php
function field_info_instance_settings($type)
```

## Documentation

```text
Returns a field type's default instance settings.

@param $type
  A field type name.

@return
  The field type's default instance settings, as provided by
  hook_field_info(), or an empty array if type or settings are not defined.
```

## Code

```php
function field_info_instance_settings($type) {
  $info = field_info_field_types($type);
  return isset($info['instance_settings']) ? $info['instance_settings'] : array();
}
```

---
_Drupal 7.103 · [modules/field/field.info.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
