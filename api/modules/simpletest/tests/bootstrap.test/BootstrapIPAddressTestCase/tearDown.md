# BootstrapIPAddressTestCase::tearDown()

- **Type:** Method
- **File:** [`modules/simpletest/tests/bootstrap.test`](../_file.md), lines 39–43 · [local source](../../../../../../source/modules/simpletest/tests/bootstrap.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test#L39-L43)
- **Class:** [BootstrapIPAddressTestCase](../BootstrapIPAddressTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function tearDown()
```

## Documentation

_No docblock in source._

## Code

```php
  function tearDown() {
    $_SERVER = $this->oldserver;
    drupal_static_reset('ip_address');
    parent::tearDown();
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/bootstrap.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test) · Licensed GPL-2.0-or-later (see LICENSE)._
