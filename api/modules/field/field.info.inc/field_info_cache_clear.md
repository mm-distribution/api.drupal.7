# field_info_cache_clear()

- **Type:** Function
- **File:** [`modules/field/field.info.inc`](_file.md), lines 54–64 · [local source](../../../../source/modules/field/field.info.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc#L54-L64)
- **Module/theme:** field
- **Topics:** [field_info](../../../topics/field_info.md)

## Signature

```php
function field_info_cache_clear()
```

## Documentation

```text
Clears the field info cache without clearing the field data cache.

This is useful when deleted fields or instances are purged.  We
need to remove the purged records, but no actual field data items
are affected.
```

## Code

```php
function field_info_cache_clear() {
  drupal_static_reset('field_view_mode_settings');
  drupal_static_reset('field_available_languages');

  // @todo: Remove this when field_attach_*_bundle() bundle management
  // functions are moved to the entity API.
  entity_info_cache_clear();

  _field_info_collate_types(TRUE);
  _field_info_field_cache()->flush();
}
```

---
_Drupal 7.103 · [modules/field/field.info.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
