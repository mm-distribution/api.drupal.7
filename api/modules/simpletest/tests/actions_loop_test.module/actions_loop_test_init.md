# actions_loop_test_init()

- **Type:** Function
- **File:** [`modules/simpletest/tests/actions_loop_test.module`](_file.md), lines 40–44 · [local source](../../../../../source/modules/simpletest/tests/actions_loop_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/actions_loop_test.module#L40-L44)
- **Module/theme:** batch_test
- **Implements:** [hook_init()](../../../system/system.api.php/hook_init.md)

## Signature

```php
function actions_loop_test_init()
```

## Documentation

```text
Implements hook_init().
```

## Code

```php
function actions_loop_test_init() {
  if (!empty($_GET['trigger_actions_on_watchdog'])) {
    watchdog_skip_semaphore('actions_loop_test', 'Triggering action loop');
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/actions_loop_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/actions_loop_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
