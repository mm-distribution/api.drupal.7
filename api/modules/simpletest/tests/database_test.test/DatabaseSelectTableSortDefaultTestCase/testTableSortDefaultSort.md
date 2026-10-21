# DatabaseSelectTableSortDefaultTestCase::testTableSortDefaultSort()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 2780–2784 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2780-L2784)
- **Class:** [DatabaseSelectTableSortDefaultTestCase](../DatabaseSelectTableSortDefaultTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testTableSortDefaultSort()
```

## Documentation

```text
Confirm that if a sort is not set in a tableselect form there is no error thrown when using the default.
```

## Code

```php
  function testTableSortDefaultSort() {
    $this->drupalGet('database_test/tablesort_default_sort');
    // Any PHP errors or notices thrown would trigger a simpletest exception, so
    // no additional assertions are needed.
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
