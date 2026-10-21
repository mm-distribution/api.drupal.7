# DatabaseSelectComplexTestCase::testCountQueryRemovals()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 2332–2354 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2332-L2354)
- **Class:** [DatabaseSelectComplexTestCase](../DatabaseSelectComplexTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testCountQueryRemovals()
```

## Documentation

```text
Test that countQuery properly removes 'all_fields' statements and
ordering clauses.
```

## Code

```php
  function testCountQueryRemovals() {
    $query = db_select('test');
    $query->fields('test');
    $query->orderBy('name');
    $count = $query->countQuery();

    // Check that the 'all_fields' statement is handled properly.
    $tables = $query->getTables();
    $this->assertEqual($tables['test']['all_fields'], 1, 'Query correctly sets \'all_fields\' statement.');
    $tables = $count->getTables();
    $this->assertFalse(isset($tables['test']['all_fields']), 'Count query correctly unsets \'all_fields\' statement.');

    // Check that the ordering clause is handled properly.
    $orderby = $query->getOrderBy();
    $this->assertEqual($orderby['name'], 'ASC', 'Query correctly sets ordering clause.');
    $orderby = $count->getOrderBy();
    $this->assertFalse(isset($orderby['name']), 'Count query correctly unsets ordering caluse.');

    // Make sure that the count query works.
    $count = $count->execute()->fetchField();

    $this->assertEqual($count, 4, 'Counted the correct number of records.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
