# block_test_system_theme_info()

- **Type:** Function
- **File:** [`modules/block/tests/block_test.module`](_file.md), lines 11–14 · [local source](../../../../../source/modules/block/tests/block_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/tests/block_test.module#L11-L14)
- **Module/theme:** block_test
- **Implements:** [hook_system_theme_info()](../../../system/system.api.php/hook_system_theme_info.md)

## Signature

```php
function block_test_system_theme_info()
```

## Documentation

```text
Implements hook_system_theme_info().
```

## Code

```php
function block_test_system_theme_info() {
  $themes['block_test_theme'] = drupal_get_path('module', 'block_test') . '/themes/block_test_theme/block_test_theme.info';
  return $themes;
}
```

---
_Drupal 7.103 · [modules/block/tests/block_test.module](https://github.com/drupal/drupal/blob/7.103/modules/block/tests/block_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
