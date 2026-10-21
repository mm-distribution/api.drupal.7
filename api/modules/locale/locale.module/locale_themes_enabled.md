# locale_themes_enabled()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 874–876 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L874-L876)
- **Module/theme:** locale
- **Implements:** [hook_themes_enabled()](../../system/theme.api.php/hook_themes_enabled.md)

## Signature

```php
function locale_themes_enabled($themes)
```

## Documentation

```text
Implements hook_themes_enabled().

@todo This is technically wrong. We must not import upon enabling, but upon
  initial installation. The theme system is missing an installation hook.
```

## Code

```php
function locale_themes_enabled($themes) {
  locale_system_update($themes);
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
