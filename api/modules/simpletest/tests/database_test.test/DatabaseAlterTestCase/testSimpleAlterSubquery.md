# DatabaseAlterTestCase::testSimpleAlterSubquery()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 3051–3071 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L3051-L3071)
- **Class:** [DatabaseAlterTestCase](../DatabaseAlterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testSimpleAlterSubquery()
```

## Documentation

```text
Test that we can do basic alters on subqueries.
```

## Code

```php
  function testSimpleAlterSubquery() {
    // Create a sub-query with an alter tag.
    $subquery = db_select('test', 'p');
    $subquery->addField('p', 'name');
    $subquery->addField('p', 'id');
    // Pick out George.
    $subquery->condition('age', 27);
    $subquery->addExpression("age*2", 'double_age');
    // This query alter should change it to age * 3.
    $subquery->addTag('database_test_alter_change_expressions');

    // Create a main query and join to sub-query.
    $query = db_select('test_task', 'tt');
    $query->join($subquery, 'pq', 'pq.id = tt.pid');
    $age_field = $query->addField('pq', 'double_age');
    $name_field = $query->addField('pq', 'name');

    $record = $query->execute()->fetch();
    $this->assertEqual($record->$name_field, 'George', 'Fetched name is correct.');
    $this->assertEqual($record->$age_field, 27*3, 'Fetched age expression is correct.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
