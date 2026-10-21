# UpdateDependencyHookInvocationTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/update.test`](../_file.md), lines 100–103 · [local source](../../../../../../source/modules/simpletest/tests/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/update.test#L100-L103)
- **Class:** [UpdateDependencyHookInvocationTestCase](../UpdateDependencyHookInvocationTestCase.md)
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
    parent::setUp('update_test_1', 'update_test_2');
    require_once DRUPAL_ROOT . '/includes/update.inc';
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/update.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
