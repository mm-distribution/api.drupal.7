# hook_boot()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 1875–1879 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L1875-L1879)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_boot()
```

## Documentation

```text
Perform setup tasks for all page requests.

This hook is run at the beginning of the page request. It is typically
used to set up global parameters that are needed later in the request.

Only use this hook if your code must run even for cached page views. This
hook is called before the theme, modules, or most include files are loaded
into memory. It happens while Drupal is still in bootstrap mode.

@see hook_init()
```

## Code

```php
function hook_boot() {
  // We need user_access() in the shutdown function. Make sure it gets loaded.
  drupal_load('module', 'user');
  drupal_register_shutdown_function('devel_shutdown');
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_boot()".

- [boot_test_1_boot()](../../simpletest/tests/boot_test_1.module/boot_test_1_boot.md) — `modules/simpletest/tests/boot_test_1.module`
- [session_test_boot()](../../simpletest/tests/session_test.module/session_test_boot.md) — `modules/simpletest/tests/session_test.module`
- [system_test_boot()](../../simpletest/tests/system_test.module/system_test_boot.md) — `modules/simpletest/tests/system_test.module`
- [locale_test_boot()](../../locale/tests/locale_test.module/locale_test_boot.md) — `modules/locale/tests/locale_test.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
