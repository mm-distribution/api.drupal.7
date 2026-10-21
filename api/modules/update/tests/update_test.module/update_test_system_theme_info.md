# update_test_system_theme_info()

- **Type:** Function
- **File:** [`modules/update/tests/update_test.module`](_file.md), lines 11–16 · [local source](../../../../../source/modules/update/tests/update_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/tests/update_test.module#L11-L16)
- **Module/theme:** aaa_update_test
- **Implements:** [hook_system_theme_info()](../../../system/system.api.php/hook_system_theme_info.md)

## Signature

```php
function update_test_system_theme_info()
```

## Documentation

```text
Implements hook_system_theme_info().
```

## Code

```php
function update_test_system_theme_info() {
  $themes['update_test_basetheme'] = drupal_get_path('module', 'update_test') . '/themes/update_test_basetheme/update_test_basetheme.info';
  $themes['update_test_subtheme'] = drupal_get_path('module', 'update_test') . '/themes/update_test_subtheme/update_test_subtheme.info';
  $themes['update_test_admintheme'] = drupal_get_path('module', 'update_test') . '/themes/update_test_admintheme/update_test_admintheme.info';
  return $themes;
}
```

---
_Drupal 7.103 · [modules/update/tests/update_test.module](https://github.com/drupal/drupal/blob/7.103/modules/update/tests/update_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
