# hook_exit()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 728–733 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L728-L733)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_exit($destination = NULL)
```

## Documentation

```text
Perform cleanup tasks.

This hook is run at the end of most regular page requests. It is often
used for page logging and specialized cleanup. This hook MUST NOT print
anything because by the time it runs the response is already sent to
the browser.

Only use this hook if your code must run even for cached page views.
If you have code which must run once on all non-cached pages, use
hook_init() instead. That is the usual case. If you implement this hook
and see an error like 'Call to undefined function', it is likely that
you are depending on the presence of a module which has not been loaded yet.
It is not loaded because Drupal is still in bootstrap mode.

@param $destination
  If this hook is invoked as part of a drupal_goto() call, then this argument
  will be a fully-qualified URL that is the destination of the redirect.
```

## Code

```php
function hook_exit($destination = NULL) {
  db_update('counter')
    ->expression('hits', 'hits + 1')
    ->condition('type', 1)
    ->execute();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_exit()".

- [system_test_exit()](../../simpletest/tests/system_test.module/system_test_exit.md) — `modules/simpletest/tests/system_test.module`
- [theme_test_exit()](../../simpletest/tests/theme_test.module/theme_test_exit.md) — `modules/simpletest/tests/theme_test.module`
- [overlay_exit()](../../overlay/overlay.module/overlay_exit.md) — `modules/overlay/overlay.module`
- [statistics_exit()](../../statistics/statistics.module/statistics_exit.md) — `modules/statistics/statistics.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
