# locale_modules_enabled()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 641–645 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L641-L645)
- **Module/theme:** locale
- **Implements:** [hook_modules_enabled()](../../system/system.api.php/hook_modules_enabled.md)

## Signature

```php
function locale_modules_enabled($modules)
```

## Documentation

```text
Implements hook_modules_enabled().
```

## Code

```php
function locale_modules_enabled($modules) {
  include_once DRUPAL_ROOT . '/includes/language.inc';
  language_types_set();
  language_negotiation_purge();
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
