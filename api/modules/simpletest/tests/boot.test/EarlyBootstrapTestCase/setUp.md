# EarlyBootstrapTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/boot.test`](../_file.md), lines 15–17 · [local source](../../../../../../source/modules/simpletest/tests/boot.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/boot.test#L15-L17)
- **Class:** [EarlyBootstrapTestCase](../EarlyBootstrapTestCase.md)
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
    parent::setUp('boot_test_1', 'boot_test_2');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/boot.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/boot.test) · Licensed GPL-2.0-or-later (see LICENSE)._
