# DatabaseSelectSubqueryTestCase::testFromSubquerySelect()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 1868–1897 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L1868-L1897)
- **Class:** [DatabaseSelectSubqueryTestCase](../DatabaseSelectSubqueryTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testFromSubquerySelect()
```

## Documentation

```text
Test that we can use a subquery in a FROM clause.
```

## Code

```php
  function testFromSubquerySelect() {
    // Create a subquery, which is just a normal query object.
    $subquery = db_select('test_task', 'tt');
    $subquery->addField('tt', 'pid', 'pid');
    $subquery->addField('tt', 'task', 'task');
    $subquery->condition('priority', 1);

    for ($i = 0; $i < 2; $i++) {
      // Create another query that joins against the virtual table resulting
      // from the subquery.
      $select = db_select($subquery, 'tt2');
      $select->join('test', 't', 't.id=tt2.pid');
      $select->addField('t', 'name');
      if ($i) {
        // Use a different number of conditions here to confuse the subquery
        // placeholder counter, testing http://drupal.org/node/1112854.
        $select->condition('name', 'John');
      }
      $select->condition('task', 'code');

      // The resulting query should be equivalent to:
      // SELECT t.name
      // FROM (SELECT tt.pid AS pid, tt.task AS task FROM test_task tt WHERE priority=1) tt
      //   INNER JOIN test t ON t.id=tt.pid
      // WHERE tt.task = 'code'
      $people = $select->execute()->fetchCol();

      $this->assertEqual(count($people), 1, 'Returned the correct number of rows.');
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
