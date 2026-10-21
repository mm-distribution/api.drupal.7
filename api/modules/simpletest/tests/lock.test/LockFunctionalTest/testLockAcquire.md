# LockFunctionalTest::testLockAcquire()

- **Type:** Method
- **File:** [`modules/simpletest/tests/lock.test`](../_file.md), lines 23–55 · [local source](../../../../../../source/modules/simpletest/tests/lock.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/lock.test#L23-L55)
- **Class:** [LockFunctionalTest](../LockFunctionalTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testLockAcquire()
```

## Documentation

```text
Confirm that we can acquire and release locks in two parallel requests.
```

## Code

```php
  function testLockAcquire() {
    $lock_acquired = 'TRUE: Lock successfully acquired in system_test_lock_acquire()';
    $lock_not_acquired = 'FALSE: Lock not acquired in system_test_lock_acquire()';
    $this->assertTrue(lock_acquire('system_test_lock_acquire'), 'Lock acquired by this request.', 'Lock');
    $this->assertTrue(lock_acquire('system_test_lock_acquire'), 'Lock extended by this request.', 'Lock');
    lock_release('system_test_lock_acquire');

    // Cause another request to acquire the lock.
    $this->drupalGet('system-test/lock-acquire');
    $this->assertText($lock_acquired, 'Lock acquired by the other request.', 'Lock');
    // The other request has finished, thus it should have released its lock.
    $this->assertTrue(lock_acquire('system_test_lock_acquire'), 'Lock acquired by this request.', 'Lock');
    // This request holds the lock, so the other request cannot acquire it.
    $this->drupalGet('system-test/lock-acquire');
    $this->assertText($lock_not_acquired, 'Lock not acquired by the other request.', 'Lock');
    lock_release('system_test_lock_acquire');

    // Try a very short timeout and lock breaking.
    $this->assertTrue(lock_acquire('system_test_lock_acquire', 0.5), 'Lock acquired by this request.', 'Lock');
    sleep(1);
    // The other request should break our lock.
    $this->drupalGet('system-test/lock-acquire');
    $this->assertText($lock_acquired, 'Lock acquired by the other request, breaking our lock.', 'Lock');
    // We cannot renew it, since the other thread took it.
    $this->assertFalse(lock_acquire('system_test_lock_acquire'), 'Lock cannot be extended by this request.', 'Lock');

    // Check the shut-down function.
    $lock_acquired_exit = 'TRUE: Lock successfully acquired in system_test_lock_exit()';
    $lock_not_acquired_exit = 'FALSE: Lock not acquired in system_test_lock_exit()';
    $this->drupalGet('system-test/lock-exit');
    $this->assertText($lock_acquired_exit, 'Lock acquired by the other request before exit.', 'Lock');
    $this->assertTrue(lock_acquire('system_test_lock_exit'), 'Lock acquired by this request after the other request exits.', 'Lock');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/lock.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/lock.test) · Licensed GPL-2.0-or-later (see LICENSE)._
