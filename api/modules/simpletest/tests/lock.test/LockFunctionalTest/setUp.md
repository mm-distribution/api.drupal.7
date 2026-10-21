# LockFunctionalTest::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/lock.test`](../_file.md), lines 16–18 · [local source](../../../../../../source/modules/simpletest/tests/lock.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/lock.test#L16-L18)
- **Class:** [LockFunctionalTest](../LockFunctionalTest.md)
- **Module/theme:** batch_test

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('system_test');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/lock.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/lock.test) · Licensed GPL-2.0-or-later (see LICENSE)._
