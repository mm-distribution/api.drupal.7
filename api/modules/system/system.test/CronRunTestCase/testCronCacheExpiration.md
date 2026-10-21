# CronRunTestCase::testCronCacheExpiration()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 949–964 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L949-L964)
- **Class:** [CronRunTestCase](../CronRunTestCase.md)
- **Module/theme:** system

## Signature

```php
public function testCronCacheExpiration()
```

## Documentation

```text
Tests that hook_flush_caches() is not invoked on every single cron run.

@see system_cron()
```

## Code

```php
  public function testCronCacheExpiration() {
    module_enable(array('system_cron_test'));
    variable_del('system_cron_test_flush_caches');

    // Invoke cron the first time: hook_flush_caches() should be called and then
    // get cached.
    drupal_cron_run();
    $this->assertEqual(variable_get('system_cron_test_flush_caches'), 1, 'hook_flush_caches() was invoked the first time.');
    $cache = cache_get('system_cache_tables');
    $this->assertEqual(empty($cache), FALSE, 'Cache is filled with cache table data.');

    // Run cron again and ensure that hook_flush_caches() is not called.
    variable_del('system_cron_test_flush_caches');
    drupal_cron_run();
    $this->assertNull(variable_get('system_cron_test_flush_caches'), 'hook_flush_caches() was not invoked the second time.');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
