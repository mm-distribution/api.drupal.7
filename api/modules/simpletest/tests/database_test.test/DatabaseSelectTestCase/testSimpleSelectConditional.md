# DatabaseSelectTestCase::testSimpleSelectConditional()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 1535–1550 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L1535-L1550)
- **Class:** [DatabaseSelectTestCase](../DatabaseSelectTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testSimpleSelectConditional()
```

## Documentation

```text
Test basic conditionals on SELECT statements.
```

## Code

```php
  function testSimpleSelectConditional() {
    $query = db_select('test');
    $name_field = $query->addField('test', 'name');
    $age_field = $query->addField('test', 'age', 'age');
    $query->condition('age', 27);
    $result = $query->execute();

    // Check that the aliases are being created the way we want.
    $this->assertEqual($name_field, 'name', 'Name field alias is correct.');
    $this->assertEqual($age_field, 'age', 'Age field alias is correct.');

    // Ensure that we got the right record.
    $record = $result->fetch();
    $this->assertEqual($record->$name_field, 'George', 'Fetched name is correct.');
    $this->assertEqual($record->$age_field, 27, 'Fetched age is correct.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
