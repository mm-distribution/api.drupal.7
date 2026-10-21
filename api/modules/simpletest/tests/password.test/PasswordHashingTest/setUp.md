# PasswordHashingTest::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/password.test`](../_file.md), lines 22–25 · [local source](../../../../../../source/modules/simpletest/tests/password.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/password.test#L22-L25)
- **Class:** [PasswordHashingTest](../PasswordHashingTest.md)
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
    require_once DRUPAL_ROOT . '/' . variable_get('password_inc', 'includes/password.inc');
    parent::setUp();
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/password.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/password.test) · Licensed GPL-2.0-or-later (see LICENSE)._
