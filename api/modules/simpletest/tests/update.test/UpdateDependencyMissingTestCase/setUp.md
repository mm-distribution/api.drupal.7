# UpdateDependencyMissingTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/update.test`](../_file.md), lines 70–75 · [local source](../../../../../../source/modules/simpletest/tests/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/update.test#L70-L75)
- **Class:** [UpdateDependencyMissingTestCase](../UpdateDependencyMissingTestCase.md)
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
    // Only install update_test_2.module, even though its updates have a
    // dependency on update_test_3.module.
    parent::setUp('update_test_2');
    require_once DRUPAL_ROOT . '/includes/update.inc';
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/update.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
