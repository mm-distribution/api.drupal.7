# field_flush_caches()

- **Type:** Function
- **File:** [`modules/field/field.module`](_file.md), lines 400–406 · [local source](../../../../source/modules/field/field.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module#L400-L406)
- **Module/theme:** field
- **Topics:** [field](../../../topics/field.md)
- **Implements:** [hook_flush_caches()](../../system/system.api.php/hook_flush_caches.md)

## Signature

```php
function field_flush_caches()
```

## Documentation

```text
Implements hook_flush_caches().
```

## Code

```php
function field_flush_caches() {
  // Refresh the 'active' status of fields.
  field_sync_field_status();

  // Request a flush of our cache table.
  return array('cache_field');
}
```

---
_Drupal 7.103 · [modules/field/field.module](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module) · Licensed GPL-2.0-or-later (see LICENSE)._
