# DatabaseSelectSubqueryTestCase::testExistsSubquerySelect()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 1978–2000 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L1978-L2000)
- **Class:** [DatabaseSelectSubqueryTestCase](../DatabaseSelectSubqueryTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testExistsSubquerySelect()
```

## Documentation

```text
Test EXISTS subquery conditionals on SELECT statements.

We essentially select all rows from the {test} table that have matching
rows in the {test_people} table based on the shared name column.
```

## Code

```php
  function testExistsSubquerySelect() {
    // Put George into {test_people}.
    db_insert('test_people')
      ->fields(array(
        'name' => 'George',
        'age' => 27,
        'job' => 'Singer',
      ))
      ->execute();
    // Base query to {test}.
    $query = db_select('test', 't')
      ->fields('t', array('name'));
    // Subquery to {test_people}.
    $subquery = db_select('test_people', 'tp')
      ->fields('tp', array('name'))
      ->where('tp.name = t.name');
    $query->exists($subquery);
    $result = $query->execute();

    // Ensure that we got the right record.
    $record = $result->fetch();
    $this->assertEqual($record->name, 'George', 'Fetched name is correct using EXISTS query.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
