# field_info_storage_settings()

- **Type:** Function
- **File:** [`modules/field/field.info.inc`](_file.md), lines 809–812 · [local source](../../../../source/modules/field/field.info.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc#L809-L812)
- **Module/theme:** field
- **Topics:** [field_info](../../../topics/field_info.md)

## Signature

```php
function field_info_storage_settings($type)
```

## Documentation

```text
Returns a field storage type's default settings.

@param $type
  A field storage type name.

@return
  The storage type's default settings, as provided by
  hook_field_storage_info(), or an empty array if type or settings are
  undefined.
```

## Code

```php
function field_info_storage_settings($type) {
  $info = field_info_storage_types($type);
  return isset($info['settings']) ? $info['settings'] : array();
}
```

---
_Drupal 7.103 · [modules/field/field.info.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
