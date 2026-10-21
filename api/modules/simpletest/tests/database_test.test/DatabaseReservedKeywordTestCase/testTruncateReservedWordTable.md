# DatabaseReservedKeywordTestCase::testTruncateReservedWordTable()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 4607–4611 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L4607-L4611)
- **Class:** [DatabaseReservedKeywordTestCase](../DatabaseReservedKeywordTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testTruncateReservedWordTable()
```

## Documentation

_No docblock in source._

## Code

```php
  function testTruncateReservedWordTable() {
    db_truncate('virtual')->execute();
    $num_records_after = db_query("SELECT COUNT(*) FROM {virtual}")->fetchField();
    $this->assertEqual(0, $num_records_after, 'Truncated a table with a reserved name.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
