# DrupalErrorHandlerTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/error.test`](../_file.md), lines 15–17 · [local source](../../../../../../source/modules/simpletest/tests/error.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/error.test#L15-L17)
- **Class:** [DrupalErrorHandlerTestCase](../DrupalErrorHandlerTestCase.md)
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
    parent::setUp('error_test');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/error.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/error.test) · Licensed GPL-2.0-or-later (see LICENSE)._
