# actions_loop_test_log()

- **Type:** Function
- **File:** [`modules/simpletest/tests/actions_loop_test.module`](_file.md), lines 63–67 · [local source](../../../../../source/modules/simpletest/tests/actions_loop_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/actions_loop_test.module#L63-L67)
- **Module/theme:** batch_test

## Signature

```php
function actions_loop_test_log()
```

## Documentation

```text
Write a message to the log.
```

## Code

```php
function actions_loop_test_log() {
  $count = &drupal_static(__FUNCTION__, 0);
  $count++;
  watchdog_skip_semaphore('actions_loop_test', "Test log #$count");
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/actions_loop_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/actions_loop_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
