# hook_init()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 1896–1902 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L1896-L1902)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_init()
```

## Documentation

```text
Perform setup tasks for non-cached page requests.

This hook is run at the beginning of the page request. It is typically
used to set up global parameters that are needed later in the request.
When this hook is called, the theme and all modules are already loaded in
memory.

This hook is not run on cached pages.

To add CSS or JS files that should be present on all pages, modules should
not implement this hook, but declare these files in their .info file.

@see hook_boot()
```

## Code

```php
function hook_init() {
  // Since this file should only be loaded on the front page, it cannot be
  // declared in the info file.
  if (drupal_is_front_page()) {
    drupal_add_css(drupal_get_path('module', 'foo') . '/foo.css');
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_init()".

- [phptemplate_init()](../../../themes/engines/phptemplate/phptemplate.engine/phptemplate_init.md) — `themes/engines/phptemplate/phptemplate.engine`
- [actions_loop_test_init()](../../simpletest/tests/actions_loop_test.module/actions_loop_test_init.md) — `modules/simpletest/tests/actions_loop_test.module`
- [common_test_init()](../../simpletest/tests/common_test.module/common_test_init.md) — `modules/simpletest/tests/common_test.module`
- [menu_test_init()](../../simpletest/tests/menu_test.module/menu_test_init.md) — `modules/simpletest/tests/menu_test.module`
- [system_test_init()](../../simpletest/tests/system_test.module/system_test_init.md) — `modules/simpletest/tests/system_test.module`
- [theme_test_init()](../../simpletest/tests/theme_test.module/theme_test_init.md) — `modules/simpletest/tests/theme_test.module`
- [dblog_init()](../../dblog/dblog.module/dblog_init.md) — `modules/dblog/dblog.module`
- [locale_init()](../../locale/locale.module/locale_init.md) — `modules/locale/locale.module`
- [locale_test_init()](../../locale/tests/locale_test.module/locale_test_init.md) — `modules/locale/tests/locale_test.module`
- [overlay_init()](../../overlay/overlay.module/overlay_init.md) — `modules/overlay/overlay.module`
- [system_init()](../system.module/system_init.md) — `modules/system/system.module`
- [update_init()](../../update/update.module/update_init.md) — `modules/update/update.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
