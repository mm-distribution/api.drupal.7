# hook_themes_disabled()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/theme.api.php`](_file.md), lines 237–240 · [local source](../../../../source/modules/system/theme.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/theme.api.php#L237-L240)
- **Module/theme:** system

## Signature

```php
function hook_themes_disabled($theme_list)
```

## Documentation

```text
Respond to themes being disabled.

@param array $theme_list
  Array containing the names of the themes being disabled.

@see theme_disable()
```

## Code

```php
function hook_themes_disabled($theme_list) {
 // Clear all update module caches.
  _update_cache_clear();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_themes_disabled()".

- [update_themes_disabled()](../../update/update.module/update_themes_disabled.md) — `modules/update/update.module`

---
_Drupal 7.103 · [modules/system/theme.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/theme.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
