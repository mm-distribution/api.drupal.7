# system_test_lock_acquire()

- **Type:** Function
- **File:** [`modules/simpletest/tests/system_test.module`](_file.md), lines 381–389 · [local source](../../../../../source/modules/simpletest/tests/system_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module#L381-L389)
- **Module/theme:** batch_test

## Signature

```php
function system_test_lock_acquire()
```

## Documentation

```text
Try to acquire a named lock and report the outcome.
```

## Code

```php
function system_test_lock_acquire() {
  if (lock_acquire('system_test_lock_acquire')) {
    lock_release('system_test_lock_acquire');
    return 'TRUE: Lock successfully acquired in system_test_lock_acquire()';
  }
  else {
    return 'FALSE: Lock not acquired in system_test_lock_acquire()';
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/system_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
