# _system_themes_access()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 1727–1729 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L1727-L1729)
- **Module/theme:** system

## Signature

```php
function _system_themes_access($theme)
```

## Documentation

```text
Menu item access callback - only admin or enabled themes can be accessed.
```

## Code

```php
function _system_themes_access($theme) {
  return user_access('administer themes') && drupal_theme_access($theme);
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
