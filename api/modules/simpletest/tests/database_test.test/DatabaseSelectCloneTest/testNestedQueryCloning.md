# DatabaseSelectCloneTest::testNestedQueryCloning()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 348–370 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L348-L370)
- **Class:** [DatabaseSelectCloneTest](../DatabaseSelectCloneTest.md)
- **Module/theme:** batch_test

## Signature

```php
public function testNestedQueryCloning()
```

## Documentation

```text
Tests that nested SELECT queries are cloned properly.
```

## Code

```php
  public function testNestedQueryCloning() {
    $sub_query = db_select('test', 't');
    $sub_query->addField('t', 'id', 'id');
    $sub_query->condition('age', 28, '<');

    $query = db_select($sub_query, 't');

    $clone = clone $query;

    // Cloned query should have a different unique identifier.
    $this->assertNotEqual($query->uniqueIdentifier(), $clone->uniqueIdentifier());

    // Cloned query should not be altered by the following modification
    // happening on original query.
    $sub_query->condition('age', 25, '>');

    $clone_result = $clone->countQuery()->execute()->fetchField();
    $query_result = $query->countQuery()->execute()->fetchField();

    // Make sure the cloned query has not been modified.
    $this->assertEqual(3, $clone_result, 'The cloned query returns the expected number of rows');
    $this->assertEqual(2, $query_result, 'The query returns the expected number of rows');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
