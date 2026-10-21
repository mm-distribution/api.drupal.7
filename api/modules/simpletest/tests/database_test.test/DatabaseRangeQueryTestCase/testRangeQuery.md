# DatabaseRangeQueryTestCase::testRangeQuery()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 3307–3316 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L3307-L3316)
- **Class:** [DatabaseRangeQueryTestCase](../DatabaseRangeQueryTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testRangeQuery()
```

## Documentation

```text
Confirm that range query work and return correct result.
```

## Code

```php
  function testRangeQuery() {
    // Test if return correct number of rows.
    $range_rows = db_query_range("SELECT name FROM {system} ORDER BY name", 2, 3)->fetchAll();
    $this->assertEqual(count($range_rows), 3, 'Range query work and return correct number of rows.');

    // Test if return target data.
    $raw_rows = db_query('SELECT name FROM {system} ORDER BY name')->fetchAll();
    $raw_rows = array_slice($raw_rows, 2, 3);
    $this->assertEqual($range_rows, $raw_rows, 'Range query work and return target data.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
