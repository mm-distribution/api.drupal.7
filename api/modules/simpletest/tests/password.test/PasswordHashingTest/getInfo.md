# PasswordHashingTest::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/password.test`](../_file.md), lines 14–20 · [local source](../../../../../../source/modules/simpletest/tests/password.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/password.test#L14-L20)
- **Class:** [PasswordHashingTest](../PasswordHashingTest.md)
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
      'name' => 'Password hashing',
      'description' => 'Password hashing unit tests.',
      'group' => 'System',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/password.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/password.test) · Licensed GPL-2.0-or-later (see LICENSE)._
