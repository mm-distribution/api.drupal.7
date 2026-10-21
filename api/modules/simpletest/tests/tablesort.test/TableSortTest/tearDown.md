# TableSortTest::tearDown()

- **Type:** Method
- **File:** [`modules/simpletest/tests/tablesort.test`](../_file.md), lines 35–40 · [local source](../../../../../../source/modules/simpletest/tests/tablesort.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/tablesort.test#L35-L40)
- **Class:** [TableSortTest](../TableSortTest.md)
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
    // Revert $_GET.
    $_GET = $this->GET;

    parent::tearDown();
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/tablesort.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/tablesort.test) · Licensed GPL-2.0-or-later (see LICENSE)._
