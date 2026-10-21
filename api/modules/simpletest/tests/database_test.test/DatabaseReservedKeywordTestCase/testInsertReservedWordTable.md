# DatabaseReservedKeywordTestCase::testInsertReservedWordTable()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 4589–4598 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L4589-L4598)
- **Class:** [DatabaseReservedKeywordTestCase](../DatabaseReservedKeywordTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testInsertReservedWordTable()
```

## Documentation

_No docblock in source._

## Code

```php
  public function testInsertReservedWordTable() {
    $num_records_before = db_query('SELECT COUNT(*) FROM {virtual}')->fetchField();
    db_insert('virtual')
      ->fields(array(
        'function' => 'Inserted function',
      ))
      ->execute();
    $num_records_after = db_query('SELECT COUNT(*) FROM {virtual}')->fetchField();
    $this->assertIdentical($num_records_before + 1, (int) $num_records_after, 'Successful insert into a table with a name and column which are reserved words.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
