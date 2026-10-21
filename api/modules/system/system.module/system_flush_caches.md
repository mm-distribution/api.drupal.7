# system_flush_caches()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 3147–3152 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L3147-L3152)
- **Module/theme:** system
- **Implements:** [hook_flush_caches()](../system.api.php/hook_flush_caches.md)

## Signature

```php
function system_flush_caches()
```

## Documentation

```text
Implements hook_flush_caches().
```

## Code

```php
function system_flush_caches() {
  // Rebuild list of date formats.
  system_date_formats_rebuild();
  // Reset the menu static caches.
  menu_reset_static_cache();
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
