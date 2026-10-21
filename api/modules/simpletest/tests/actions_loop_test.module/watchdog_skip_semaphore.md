# watchdog_skip_semaphore()

- **Type:** Function
- **File:** [`modules/simpletest/tests/actions_loop_test.module`](_file.md), lines 73–95 · [local source](../../../../../source/modules/simpletest/tests/actions_loop_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/actions_loop_test.module#L73-L95)
- **Module/theme:** batch_test

## Signature

```php
function watchdog_skip_semaphore($type, $message, $variables = array(), $severity = WATCHDOG_NOTICE, $link = NULL)
```

## Documentation

```text
Replacement of the watchdog() function that eliminates the use of semaphores
so that we can test the abortion of an action loop.
```

## Code

```php
function watchdog_skip_semaphore($type, $message, $variables = array(), $severity = WATCHDOG_NOTICE, $link = NULL) {
  global $user, $base_root;

  // Prepare the fields to be logged
  $log_entry = array(
    'type'        => $type,
    'message'     => $message,
    'variables'   => $variables,
    'severity'    => $severity,
    'link'        => $link,
    'user'        => $user,
    'uid'         => isset($user->uid) ? $user->uid : 0,
    'request_uri' => $base_root . request_uri(),
    'referer'     => $_SERVER['HTTP_REFERER'],
    'ip'          => ip_address(),
    'timestamp'   => REQUEST_TIME,
  );

  // Call the logging hooks to log/process the message
  foreach (module_implements('watchdog') as $module) {
    module_invoke($module, 'watchdog', $log_entry);
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/actions_loop_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/actions_loop_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
