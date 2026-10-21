# hook_disable()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 3670–3672 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L3670-L3672)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_disable()
```

## Documentation

```text
Perform necessary actions before module is disabled.

The hook is called every time the module is disabled. It should be
implemented in the module's .install file. The implementation can rely
on the .module file being loaded.

@see hook_uninstall()
@see hook_modules_disabled()
```

## Code

```php
function hook_disable() {
  mymodule_cache_rebuild();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_disable()".

- [dashboard_disable()](../../dashboard/dashboard.install/dashboard_disable.md) — `modules/dashboard/dashboard.install`
- [php_disable()](../../php/php.install/php_disable.md) — `modules/php/php.install`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
