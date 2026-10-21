# update_themes_disabled()

- **Type:** Function
- **File:** [`modules/update/update.module`](_file.md), lines 338–341 · [local source](../../../../source/modules/update/update.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module#L338-L341)
- **Module/theme:** update
- **Implements:** [hook_themes_disabled()](../../system/theme.api.php/hook_themes_disabled.md)

## Signature

```php
function update_themes_disabled($themes)
```

## Documentation

```text
Implements hook_themes_disabled().

If themes are disabled, we invalidate the cache of available updates.
```

## Code

```php
function update_themes_disabled($themes) {
  // Clear all update module caches.
  _update_cache_clear();
}
```

---
_Drupal 7.103 · [modules/update/update.module](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module) · Licensed GPL-2.0-or-later (see LICENSE)._
