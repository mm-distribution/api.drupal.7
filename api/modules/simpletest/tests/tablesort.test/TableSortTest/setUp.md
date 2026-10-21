# TableSortTest::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/tablesort.test`](../_file.md), lines 28–33 · [local source](../../../../../../source/modules/simpletest/tests/tablesort.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/tablesort.test#L28-L33)
- **Class:** [TableSortTest](../TableSortTest.md)
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
    // Save the original $_GET to be restored later.
    $this->GET = $_GET;

    parent::setUp();
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/tablesort.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/tablesort.test) · Licensed GPL-2.0-or-later (see LICENSE)._
