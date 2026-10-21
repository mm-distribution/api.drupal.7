# hook_themes_enabled()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/theme.api.php`](_file.md), lines 223–227 · [local source](../../../../source/modules/system/theme.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/theme.api.php#L223-L227)
- **Module/theme:** system

## Signature

```php
function hook_themes_enabled($theme_list)
```

## Documentation

```text
Respond to themes being enabled.

@param array $theme_list
  Array containing the names of the themes being enabled.

@see theme_enable()
```

## Code

```php
function hook_themes_enabled($theme_list) {
  foreach ($theme_list as $theme) {
    block_theme_initialize($theme);
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_themes_enabled()".

- [locale_themes_enabled()](../../locale/locale.module/locale_themes_enabled.md) — `modules/locale/locale.module`
- [update_themes_enabled()](../../update/update.module/update_themes_enabled.md) — `modules/update/update.module`

---
_Drupal 7.103 · [modules/system/theme.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/theme.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
