# DatabaseSelectSubqueryTestCase::testConditionSubquerySelect()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 1928–1946 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L1928-L1946)
- **Class:** [DatabaseSelectSubqueryTestCase](../DatabaseSelectSubqueryTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testConditionSubquerySelect()
```

## Documentation

```text
Test that we can use a subquery in a WHERE clause.
```

## Code

```php
  function testConditionSubquerySelect() {
    // Create a subquery, which is just a normal query object.
    $subquery = db_select('test_task', 'tt');
    $subquery->addField('tt', 'pid', 'pid');
    $subquery->condition('tt.priority', 1);

    // Create another query that joins against the virtual table resulting
    // from the subquery.
    $select = db_select('test_task', 'tt2');
    $select->addField('tt2', 'task');
    $select->condition('tt2.pid', $subquery, 'IN');

    // The resulting query should be equivalent to:
    // SELECT tt2.name
    // FROM test tt2
    // WHERE tt2.pid IN (SELECT tt.pid AS pid FROM test_task tt WHERE tt.priority=1)
    $people = $select->execute()->fetchCol();
    $this->assertEqual(count($people), 5, 'Returned the correct number of rows.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
