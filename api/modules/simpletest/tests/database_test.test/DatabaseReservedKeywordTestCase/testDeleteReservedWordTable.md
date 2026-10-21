# DatabaseReservedKeywordTestCase::testDeleteReservedWordTable()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 4600–4605 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L4600-L4605)
- **Class:** [DatabaseReservedKeywordTestCase](../DatabaseReservedKeywordTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testDeleteReservedWordTable()
```

## Documentation

_No docblock in source._

## Code

```php
  public function testDeleteReservedWordTable() {
    $delete = db_delete('virtual')
      ->condition('function', 'Function value 1');
    $num_deleted = $delete->execute();
    $this->assertEqual($num_deleted, 1, "Deleted 1 record from a table with a name and column which are reserved words..");
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
