# DatabaseSelectSubqueryTestCase::testFromSubquerySelectWithLimit()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 1902–1923 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L1902-L1923)
- **Class:** [DatabaseSelectSubqueryTestCase](../DatabaseSelectSubqueryTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testFromSubquerySelectWithLimit()
```

## Documentation

```text
Test that we can use a subquery in a FROM clause with a limit.
```

## Code

```php
  function testFromSubquerySelectWithLimit() {
    // Create a subquery, which is just a normal query object.
    $subquery = db_select('test_task', 'tt');
    $subquery->addField('tt', 'pid', 'pid');
    $subquery->addField('tt', 'task', 'task');
    $subquery->orderBy('priority', 'DESC');
    $subquery->range(0, 1);

    // Create another query that joins against the virtual table resulting
    // from the subquery.
    $select = db_select($subquery, 'tt2');
    $select->join('test', 't', 't.id=tt2.pid');
    $select->addField('t', 'name');

    // The resulting query should be equivalent to:
    // SELECT t.name
    // FROM (SELECT tt.pid AS pid, tt.task AS task FROM test_task tt ORDER BY priority DESC LIMIT 1 OFFSET 0) tt
    //   INNER JOIN test t ON t.id=tt.pid
    $people = $select->execute()->fetchCol();

    $this->assertEqual(count($people), 1, 'Returned the correct number of rows.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
