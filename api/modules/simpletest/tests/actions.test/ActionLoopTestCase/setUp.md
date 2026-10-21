# ActionLoopTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/actions.test`](../_file.md), lines 78–80 · [local source](../../../../../../source/modules/simpletest/tests/actions.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/actions.test#L78-L80)
- **Class:** [ActionLoopTestCase](../ActionLoopTestCase.md)
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
    parent::setUp('dblog', 'trigger', 'actions_loop_test');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/actions.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/actions.test) · Licensed GPL-2.0-or-later (see LICENSE)._
