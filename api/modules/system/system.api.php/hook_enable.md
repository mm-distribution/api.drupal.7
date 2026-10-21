# hook_enable()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 3656–3658 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L3656-L3658)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_enable()
```

## Documentation

```text
Perform necessary actions after module is enabled.

The hook is called every time the module is enabled. It should be
implemented in the module's .install file. The implementation can
rely on the .module file being loaded.

@see module_enable()
@see hook_install()
@see hook_modules_enabled()
```

## Code

```php
function hook_enable() {
  mymodule_cache_rebuild();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_enable()".

- [module_test_enable()](../../simpletest/tests/module_test.install/module_test_enable.md) — `modules/simpletest/tests/module_test.install`
- [comment_enable()](../../comment/comment.install/comment_enable.md) — `modules/comment/comment.install`
- [dashboard_enable()](../../dashboard/dashboard.install/dashboard_enable.md) — `modules/dashboard/dashboard.install`
- [forum_enable()](../../forum/forum.install/forum_enable.md) — `modules/forum/forum.install`
- [menu_enable()](../../menu/menu.module/menu_enable.md) — `modules/menu/menu.module`
- [overlay_enable()](../../overlay/overlay.install/overlay_enable.md) — `modules/overlay/overlay.install`
- [php_enable()](../../php/php.install/php_enable.md) — `modules/php/php.install`
- [tracker_enable()](../../tracker/tracker.install/tracker_enable.md) — `modules/tracker/tracker.install`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
