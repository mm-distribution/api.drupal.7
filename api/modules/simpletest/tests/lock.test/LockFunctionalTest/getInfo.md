# LockFunctionalTest::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/lock.test`](../_file.md), lines 8–14 · [local source](../../../../../../source/modules/simpletest/tests/lock.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/lock.test#L8-L14)
- **Class:** [LockFunctionalTest](../LockFunctionalTest.md)
- **Module/theme:** batch_test

## Signature

```php
public static function getInfo()
```

## Documentation

_No docblock in source._

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'Locking framework tests',
      'description' => 'Confirm locking works between two separate requests.',
      'group' => 'System',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/lock.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/lock.test) · Licensed GPL-2.0-or-later (see LICENSE)._
