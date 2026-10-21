# DatabaseSelectSubqueryTestCase::testJoinSubquerySelect()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 1951–1970 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L1951-L1970)
- **Class:** [DatabaseSelectSubqueryTestCase](../DatabaseSelectSubqueryTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testJoinSubquerySelect()
```

## Documentation

```text
Test that we can use a subquery in a JOIN clause.
```

## Code

```php
  function testJoinSubquerySelect() {
    // Create a subquery, which is just a normal query object.
    $subquery = db_select('test_task', 'tt');
    $subquery->addField('tt', 'pid', 'pid');
    $subquery->condition('priority', 1);

    // Create another query that joins against the virtual table resulting
    // from the subquery.
    $select = db_select('test', 't');
    $select->join($subquery, 'tt', 't.id=tt.pid');
    $select->addField('t', 'name');

    // The resulting query should be equivalent to:
    // SELECT t.name
    // FROM test t
    //   INNER JOIN (SELECT tt.pid AS pid FROM test_task tt WHERE priority=1) tt ON t.id=tt.pid
    $people = $select->execute()->fetchCol();

    $this->assertEqual(count($people), 2, 'Returned the correct number of rows.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
