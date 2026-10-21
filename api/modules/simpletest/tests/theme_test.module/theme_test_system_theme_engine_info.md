# theme_test_system_theme_engine_info()

- **Type:** Function
- **File:** [`modules/simpletest/tests/theme_test.module`](_file.md), lines 37–40 · [local source](../../../../../source/modules/simpletest/tests/theme_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme_test.module#L37-L40)
- **Module/theme:** batch_test
- **Implements:** [hook_system_theme_engine_info()](../../../system/system.api.php/hook_system_theme_engine_info.md)

## Signature

```php
function theme_test_system_theme_engine_info()
```

## Documentation

```text
Implements hook_system_theme_engine_info().
```

## Code

```php
function theme_test_system_theme_engine_info() {
  $theme_engines['nyan_cat'] = drupal_get_path('module', 'theme_test') . '/themes/engines/nyan_cat/nyan_cat.engine';
  return $theme_engines;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
