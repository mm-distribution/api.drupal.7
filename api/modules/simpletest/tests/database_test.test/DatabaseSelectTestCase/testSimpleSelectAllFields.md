# DatabaseSelectTestCase::testSimpleSelectAllFields()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 1620–1638 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L1620-L1638)
- **Class:** [DatabaseSelectTestCase](../DatabaseSelectTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testSimpleSelectAllFields()
```

## Documentation

```text
Test adding all fields from a given table to a select statement.
```

## Code

```php
  function testSimpleSelectAllFields() {
    $record = db_select('test')
      ->fields('test')
      ->condition('age', 27)
      ->execute()->fetchObject();

    // Check that all fields we asked for are present.
    $this->assertNotNull($record->id, 'ID field is present.');
    $this->assertNotNull($record->name, 'Name field is present.');
    $this->assertNotNull($record->age, 'Age field is present.');
    $this->assertNotNull($record->job, 'Job field is present.');

    // Ensure that we got the right record.
    // Check that all fields we asked for are present.
    $this->assertEqual($record->id, 2, 'ID field has the correct value.');
    $this->assertEqual($record->name, 'George', 'Name field has the correct value.');
    $this->assertEqual($record->age, 27, 'Age field has the correct value.');
    $this->assertEqual($record->job, 'Singer', 'Job field has the correct value.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
