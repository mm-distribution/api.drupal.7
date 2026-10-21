# hook_modules_installed()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 2674–2678 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L2674-L2678)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_modules_installed($modules)
```

## Documentation

```text
Perform necessary actions after modules are installed.

This function differs from hook_install() in that it gives all other modules
a chance to perform actions when a module is installed, whereas
hook_install() is only called on the module actually being installed. See
module_enable() for a detailed description of the order in which install and
enable hooks are invoked.

This hook should be implemented in a .module file, not in an .install file.

@param $modules
  An array of the modules that were installed.

@see module_enable()
@see hook_modules_enabled()
@see hook_install()
```

## Code

```php
function hook_modules_installed($modules) {
  if (in_array('lousy_module', $modules)) {
    variable_set('lousy_module_conflicting_variable', FALSE);
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_modules_installed()".

- [system_test_modules_installed()](../../simpletest/tests/system_test.module/system_test_modules_installed.md) — `modules/simpletest/tests/system_test.module`
- [locale_modules_installed()](../../locale/locale.module/locale_modules_installed.md) — `modules/locale/locale.module`
- [rdf_modules_installed()](../../rdf/rdf.module/rdf_modules_installed.md) — `modules/rdf/rdf.module`
- [user_modules_installed()](../../user/user.module/user_modules_installed.md) — `modules/user/user.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
