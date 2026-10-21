# SimpleTestBrowserTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/simpletest.test`](../_file.md), lines 366–369 · [local source](../../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L366-L369)
- **Class:** [SimpleTestBrowserTestCase](../SimpleTestBrowserTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp();
    variable_set('user_register', USER_REGISTER_VISITORS);
  }
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
