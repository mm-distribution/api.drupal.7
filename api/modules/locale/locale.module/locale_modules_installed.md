# locale_modules_installed()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 864–866 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L864-L866)
- **Module/theme:** locale
- **Implements:** [hook_modules_installed()](../../system/system.api.php/hook_modules_installed.md)

## Signature

```php
function locale_modules_installed($modules)
```

## Documentation

```text
Implements hook_modules_installed().
```

## Code

```php
function locale_modules_installed($modules) {
  locale_system_update($modules);
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
