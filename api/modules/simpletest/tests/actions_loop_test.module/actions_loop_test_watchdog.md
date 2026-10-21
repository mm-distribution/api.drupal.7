# actions_loop_test_watchdog()

- **Type:** Function
- **File:** [`modules/simpletest/tests/actions_loop_test.module`](_file.md), lines 19–35 · [local source](../../../../../source/modules/simpletest/tests/actions_loop_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/actions_loop_test.module#L19-L35)
- **Module/theme:** batch_test
- **Implements:** [hook_watchdog()](../../../system/system.api.php/hook_watchdog.md)

## Signature

```php
function actions_loop_test_watchdog(array $log_entry)
```

## Documentation

```text
Implements hook_watchdog().
```

## Code

```php
function actions_loop_test_watchdog(array $log_entry) {
  // If the triggering actions are not explicitly enabled, abort.
  if (empty($_GET['trigger_actions_on_watchdog'])) {
    return;
  }
  // Get all the action ids assigned to the trigger on the watchdog hook's
  // "run" event.
  $aids = trigger_get_assigned_actions('watchdog');
  // We can pass in any applicable information in $context. There isn't much in
  // this case, but we'll pass in the hook name as the bare minimum.
  $context = array(
    'hook' => 'watchdog',
  );
  // Fire the actions on the associated object ($log_entry) and the context
  // variable.
  actions_do(array_keys($aids), $log_entry, $context);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/actions_loop_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/actions_loop_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
