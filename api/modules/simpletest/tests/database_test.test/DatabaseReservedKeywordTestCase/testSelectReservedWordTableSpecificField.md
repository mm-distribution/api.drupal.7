# DatabaseReservedKeywordTestCase::testSelectReservedWordTableSpecificField()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 4549–4555 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L4549-L4555)
- **Class:** [DatabaseReservedKeywordTestCase](../DatabaseReservedKeywordTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testSelectReservedWordTableSpecificField()
```

## Documentation

_No docblock in source._

## Code

```php
  public function testSelectReservedWordTableSpecificField() {
    $record = db_select('virtual')
      ->fields('virtual', array('function'))
      ->execute()
      ->fetchAssoc();
    $this->assertEqual($record['function'], 'Function value 1', 'Successfully read a field from a table with a name and column which are reserved words.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
