# update_themes_enabled()

- **Type:** Function
- **File:** [`modules/update/update.module`](_file.md), lines 328–331 · [local source](../../../../source/modules/update/update.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module#L328-L331)
- **Module/theme:** update
- **Implements:** [hook_themes_enabled()](../../system/theme.api.php/hook_themes_enabled.md)

## Signature

```php
function update_themes_enabled($themes)
```

## Documentation

```text
Implements hook_themes_enabled().

If themes are enabled, we invalidate the cache of available updates.
```

## Code

```php
function update_themes_enabled($themes) {
  // Clear all update module caches.
  _update_cache_clear();
}
```

---
_Drupal 7.103 · [modules/update/update.module](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module) · Licensed GPL-2.0-or-later (see LICENSE)._
