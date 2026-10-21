# hook_system_theme_engine_info()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 2064–2067 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L2064-L2067)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_system_theme_engine_info()
```

## Documentation

```text
Return additional theme engines provided by modules.

This hook is invoked from _system_rebuild_theme_data() and allows modules to
register additional theme engines outside of the regular 'themes/engines'
directories of a Drupal installation.

@return
  An associative array. Each key is the system name of a theme engine and
  each value is the corresponding path to the theme engine's .engine file.
```

## Code

```php
function hook_system_theme_engine_info() {
  $theme_engines['izumi'] = drupal_get_path('module', 'mymodule') . '/izumi/izumi.engine';
  return $theme_engines;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_system_theme_engine_info()".

- [theme_test_system_theme_engine_info()](../../simpletest/tests/theme_test.module/theme_test_system_theme_engine_info.md) — `modules/simpletest/tests/theme_test.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
