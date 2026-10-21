# CronRunTestCase::testCronExceptions()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 918–926 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L918-L926)
- **Class:** [CronRunTestCase](../CronRunTestCase.md)
- **Module/theme:** system

## Signature

```php
function testCronExceptions()
```

## Documentation

```text
Make sure exceptions thrown on hook_cron() don't affect other modules.
```

## Code

```php
  function testCronExceptions() {
    variable_del('common_test_cron');
    // The common_test module throws an exception. If it isn't caught, the tests
    // won't finish successfully.
    // The common_test_cron_helper module sets the 'common_test_cron' variable.
    $this->cronRun();
    $result = variable_get('common_test_cron');
    $this->assertEqual($result, 'success', 'Cron correctly handles exceptions thrown during hook_cron() invocations.');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
