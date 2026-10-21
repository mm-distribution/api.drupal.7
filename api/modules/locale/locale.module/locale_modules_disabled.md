# locale_modules_disabled()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 650–652 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L650-L652)
- **Module/theme:** locale
- **Implements:** [hook_modules_disabled()](../../system/system.api.php/hook_modules_disabled.md)

## Signature

```php
function locale_modules_disabled($modules)
```

## Documentation

```text
Implements hook_modules_disabled().
```

## Code

```php
function locale_modules_disabled($modules) {
  locale_modules_enabled($modules);
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
