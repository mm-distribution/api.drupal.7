# SessionHttpsTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/session.test`](../_file.md), lines 562–564 · [local source](../../../../../../source/modules/simpletest/tests/session.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test#L562-L564)
- **Class:** [SessionHttpsTestCase](../SessionHttpsTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  public function setUp() {
    parent::setUp('session_test');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/session.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test) · Licensed GPL-2.0-or-later (see LICENSE)._
