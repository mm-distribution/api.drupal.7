# theme_test_system_theme_info()

- **Type:** Function
- **File:** [`modules/simpletest/tests/theme_test.module`](_file.md), lines 26–32 · [local source](../../../../../source/modules/simpletest/tests/theme_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme_test.module#L26-L32)
- **Module/theme:** batch_test
- **Implements:** [hook_system_theme_info()](../../../system/system.api.php/hook_system_theme_info.md)

## Signature

```php
function theme_test_system_theme_info()
```

## Documentation

```text
Implements hook_system_theme_info().
```

## Code

```php
function theme_test_system_theme_info() {
  $themes['test_theme'] = drupal_get_path('module', 'theme_test') . '/themes/test_theme/test_theme.info';
  $themes['test_basetheme'] = drupal_get_path('module', 'theme_test') . '/themes/test_basetheme/test_basetheme.info';
  $themes['test_subtheme'] = drupal_get_path('module', 'theme_test') . '/themes/test_subtheme/test_subtheme.info';
  $themes['test_theme_nyan_cat'] = drupal_get_path('module', 'theme_test') . '/themes/test_theme_nyan_cat/test_theme_nyan_cat.info';
  return $themes;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
