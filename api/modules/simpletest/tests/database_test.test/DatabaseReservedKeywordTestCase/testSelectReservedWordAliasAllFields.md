# DatabaseReservedKeywordTestCase::testSelectReservedWordAliasAllFields()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 4581–4587 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L4581-L4587)
- **Class:** [DatabaseReservedKeywordTestCase](../DatabaseReservedKeywordTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testSelectReservedWordAliasAllFields()
```

## Documentation

_No docblock in source._

## Code

```php
  public function testSelectReservedWordAliasAllFields() {
    $record = db_select('test', 'high_priority')
      ->fields('high_priority')
      ->condition('age', 27)
      ->execute()->fetchAssoc();
    $this->assertEqual($record['name'], 'George', 'Successful all_fields query using an alias which is a reserved word.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
