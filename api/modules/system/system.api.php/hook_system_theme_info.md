# hook_system_theme_info()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 2048–2051 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L2048-L2051)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_system_theme_info()
```

## Documentation

```text
Return additional themes provided by modules.

Only use this hook for testing purposes. Use a hidden MYMODULE_test.module
to implement this hook. Testing themes should be hidden, too.

This hook is invoked from _system_rebuild_theme_data() and allows modules to
register additional themes outside of the regular 'themes' directories of a
Drupal installation.

@return
  An associative array. Each key is the system name of a theme and each value
  is the corresponding path to the theme's .info file.
```

## Code

```php
function hook_system_theme_info() {
  $themes['mymodule_test_theme'] = drupal_get_path('module', 'mymodule') . '/mymodule_test_theme/mymodule_test_theme.info';
  return $themes;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_system_theme_info()".

- [update_test_system_theme_info()](../../update/tests/update_test.module/update_test_system_theme_info.md) — `modules/update/tests/update_test.module`
- [ajax_test_system_theme_info()](../../simpletest/tests/ajax_test.module/ajax_test_system_theme_info.md) — `modules/simpletest/tests/ajax_test.module`
- [theme_test_system_theme_info()](../../simpletest/tests/theme_test.module/theme_test_system_theme_info.md) — `modules/simpletest/tests/theme_test.module`
- [block_test_system_theme_info()](../../block/tests/block_test.module/block_test_system_theme_info.md) — `modules/block/tests/block_test.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
