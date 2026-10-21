# DatabaseSelectCloneTest::testSelectConditionSubQueryCloning()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 319–343 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L319-L343)
- **Class:** [DatabaseSelectCloneTest](../DatabaseSelectCloneTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testSelectConditionSubQueryCloning()
```

## Documentation

```text
Test that subqueries as value within conditions are cloned properly.
```

## Code

```php
  function testSelectConditionSubQueryCloning() {
    $subquery = db_select('test', 't');
    $subquery->addField('t', 'id', 'id');
    $subquery->condition('age', 28, '<');

    $query = db_select('test', 't');
    $query->addField('t', 'name', 'name');
    $query->condition('id', $subquery, 'IN');

    $clone = clone $query;

    // Cloned query should have a different unique identifier.
    $this->assertNotEqual($query->uniqueIdentifier(), $clone->uniqueIdentifier());

    // Cloned query should not be altered by the following modification
    // happening on original query.
    $subquery->condition('age', 25, '>');

    $clone_result = $clone->countQuery()->execute()->fetchField();
    $query_result = $query->countQuery()->execute()->fetchField();

    // Make sure the cloned query has not been modified
    $this->assertEqual(3, $clone_result, 'The cloned query returns the expected number of rows');
    $this->assertEqual(2, $query_result, 'The query returns the expected number of rows');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
