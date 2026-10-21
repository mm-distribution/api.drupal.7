# system_test_lock_exit()

- **Type:** Function
- **File:** [`modules/simpletest/tests/system_test.module`](_file.md), lines 394–403 · [local source](../../../../../source/modules/simpletest/tests/system_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module#L394-L403)
- **Module/theme:** batch_test

## Signature

```php
function system_test_lock_exit()
```

## Documentation

```text
Try to acquire a specific lock, and then exit.
```

## Code

```php
function system_test_lock_exit() {
  if (lock_acquire('system_test_lock_exit', 900)) {
    echo 'TRUE: Lock successfully acquired in system_test_lock_exit()';
    // The shut-down function should release the lock.
    exit();
  }
  else {
    return 'FALSE: Lock not acquired in system_test_lock_exit()';
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/system_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
