# DatabaseSelectComplexTestCase2::testJoinSubquery()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 2521–2552 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2521-L2552)
- **Class:** [DatabaseSelectComplexTestCase2](../DatabaseSelectComplexTestCase2.md)
- **Module/theme:** batch_test

## Signature

```php
function testJoinSubquery()
```

## Documentation

```text
Test that we can join on a query.
```

## Code

```php
  function testJoinSubquery() {
    $acct = $this->drupalCreateUser(array('access content'));
    $this->drupalLogin($acct);

    $query = db_select('test_task', 'tt', array('target' => 'slave'));
    $query->addExpression('tt.pid + 1', 'abc');
    $query->condition('priority', 1, '>');
    $query->condition('priority', 100, '<');

    $subquery = db_select('test', 'tp');
    $subquery->join('test_one_blob', 'tpb', 'tp.id = tpb.id');
    $subquery->join('node', 'n', 'tp.id = n.nid');
    $subquery->addTag('node_access');
    $subquery->addMetaData('account', $acct);
    $subquery->addField('tp', 'id');
    $subquery->condition('age', 5, '>');
    $subquery->condition('age', 500, '<');

    $query->leftJoin($subquery, 'sq', 'tt.pid = sq.id');
    $query->join('test_one_blob', 'tb3', 'tt.pid = tb3.id');

    // Construct the query string.
    // This is the same sequence that SelectQuery::execute() goes through.
    $query->preExecute();
    $query->getArguments();
    $str = (string) $query;

    // Verify that the string only has one copy of condition placeholder 0.
    $pos = strpos($str, 'db_condition_placeholder_0', 0);
    $pos2 = strpos($str, 'db_condition_placeholder_0', $pos + 1);
    $this->assertFalse($pos2, 'Condition placeholder is not repeated.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
