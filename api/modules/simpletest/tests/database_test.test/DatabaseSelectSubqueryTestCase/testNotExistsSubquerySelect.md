# DatabaseSelectSubqueryTestCase::testNotExistsSubquerySelect()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 2008–2030 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2008-L2030)
- **Class:** [DatabaseSelectSubqueryTestCase](../DatabaseSelectSubqueryTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testNotExistsSubquerySelect()
```

## Documentation

```text
Test NOT EXISTS subquery conditionals on SELECT statements.

We essentially select all rows from the {test} table that don't have
matching rows in the {test_people} table based on the shared name column.
```

## Code

```php
  function testNotExistsSubquerySelect() {
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
    $query->notExists($subquery);

    // Ensure that we got the right number of records.
    $people = $query->execute()->fetchCol();
    $this->assertEqual(count($people), 3, 'NOT EXISTS query returned the correct results.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
