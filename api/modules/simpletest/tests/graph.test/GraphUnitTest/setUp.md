# GraphUnitTest::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/graph.test`](../_file.md), lines 20–23 · [local source](../../../../../../source/modules/simpletest/tests/graph.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/graph.test#L20-L23)
- **Class:** [GraphUnitTest](../GraphUnitTest.md)
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
    require_once DRUPAL_ROOT . '/includes/graph.inc';
    parent::setUp();
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/graph.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/graph.test) · Licensed GPL-2.0-or-later (see LICENSE)._
