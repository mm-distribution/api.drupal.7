# DatabaseReservedKeywordTestCase::testSelectReservedWordAliasSpecificFields()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 4573–4579 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L4573-L4579)
- **Class:** [DatabaseReservedKeywordTestCase](../DatabaseReservedKeywordTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testSelectReservedWordAliasSpecificFields()
```

## Documentation

_No docblock in source._

## Code

```php
  public function testSelectReservedWordAliasSpecificFields() {
    $record = db_select('test', 'high_priority')
      ->fields('high_priority', array('name'))
      ->condition('age', 27)
      ->execute()->fetchAssoc();
    $this->assertEqual($record['name'], 'George', 'Successful query using an alias which is a reserved word.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
