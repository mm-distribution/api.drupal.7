# DatabaseReservedKeywordTestCase::testSelectReservedWordTableAllFields()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 4557–4563 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L4557-L4563)
- **Class:** [DatabaseReservedKeywordTestCase](../DatabaseReservedKeywordTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testSelectReservedWordTableAllFields()
```

## Documentation

_No docblock in source._

## Code

```php
  public function testSelectReservedWordTableAllFields() {
    $record = db_select('virtual')
      ->fields('virtual')
      ->execute()
      ->fetchAssoc();
    $this->assertEqual($record['function'], 'Function value 1', 'Successful all_fields query from a table with a name and column which are reserved words.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
