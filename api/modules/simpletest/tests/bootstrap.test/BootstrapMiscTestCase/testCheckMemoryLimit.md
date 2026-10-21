# BootstrapMiscTestCase::testCheckMemoryLimit()

- **Type:** Method
- **File:** [`modules/simpletest/tests/bootstrap.test`](../_file.md), lines 763–777 · [local source](../../../../../../source/modules/simpletest/tests/bootstrap.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test#L763-L777)
- **Class:** [BootstrapMiscTestCase](../BootstrapMiscTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testCheckMemoryLimit()
```

## Documentation

```text
Tests that the drupal_check_memory_limit() function works as expected.
```

## Code

```php
  function testCheckMemoryLimit() {
    // Test that a very reasonable amount of memory is available.
    $this->assertTrue(drupal_check_memory_limit('30MB'), '30MB of memory tested available.');

    // Test an unlimited memory limit.
    // The function should always return true if the memory limit is set to -1.
    $this->assertTrue(drupal_check_memory_limit('9999999999YB', -1), 'drupal_check_memory_limit() returns TRUE when a limit of -1 (none) is supplied');

    // Test that even though we have 30MB of memory available - the function
    // returns FALSE when given an upper limit for how much memory can be used.
    $this->assertFalse(drupal_check_memory_limit('30MB', '16MB'), 'drupal_check_memory_limit() returns FALSE with a 16MB upper limit on a 30MB requirement.');

    // Test that an equal amount of memory to the amount requested returns TRUE.
    $this->assertTrue(drupal_check_memory_limit('30MB', '30MB'), 'drupal_check_memory_limit() returns TRUE when requesting 30MB on a 30MB requirement.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/bootstrap.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test) · Licensed GPL-2.0-or-later (see LICENSE)._
