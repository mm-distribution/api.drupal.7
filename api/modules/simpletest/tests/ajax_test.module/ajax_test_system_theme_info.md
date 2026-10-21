# ajax_test_system_theme_info()

- **Type:** Function
- **File:** [`modules/simpletest/tests/ajax_test.module`](_file.md), lines 37–40 · [local source](../../../../../source/modules/simpletest/tests/ajax_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_test.module#L37-L40)
- **Module/theme:** batch_test
- **Implements:** [hook_system_theme_info()](../../../system/system.api.php/hook_system_theme_info.md)

## Signature

```php
function ajax_test_system_theme_info()
```

## Documentation

```text
Implements hook_system_theme_info().
```

## Code

```php
function ajax_test_system_theme_info() {
  $themes['test_theme'] = drupal_get_path('module', 'ajax_test') . '/themes/test_theme/test_theme.info';
  return $themes;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/ajax_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
