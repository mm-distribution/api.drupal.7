# DatabaseReservedKeywordTestCase::testMergeReservedWordTable()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 4620–4629 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L4620-L4629)
- **Class:** [DatabaseReservedKeywordTestCase](../DatabaseReservedKeywordTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testMergeReservedWordTable()
```

## Documentation

_No docblock in source._

## Code

```php
  function testMergeReservedWordTable() {
    $key = db_query('SELECT id FROM {virtual} LIMIT 1')->fetchField();
    $num_records_before = db_query('SELECT COUNT(*) FROM {virtual}')->fetchField();
    db_merge('virtual')
      ->key(array('id' => $key))
      ->fields(array('function' => 'Merged function'))
      ->execute();
    $num_records_after = db_query('SELECT COUNT(*) FROM {virtual}')->fetchField();
    $this->assertIdentical($num_records_before, $num_records_after, 'Successful merge query on a table with a name and column which are reserved words.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
