# DatabaseAlterTestCase::testAlterExpression()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 3018–3031 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L3018-L3031)
- **Class:** [DatabaseAlterTestCase](../DatabaseAlterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testAlterExpression()
```

## Documentation

```text
Test that we can alter expressions in the query.
```

## Code

```php
  function testAlterExpression() {
    $query = db_select('test');
    $name_field = $query->addField('test', 'name');
    $age_field = $query->addExpression("age*2", 'double_age');
    $query->condition('age', 27);
    $query->addTag('database_test_alter_change_expressions');
    $result = $query->execute();

    // Ensure that we got the right record.
    $record = $result->fetch();

    $this->assertEqual($record->$name_field, 'George', 'Fetched name is correct.');
    $this->assertEqual($record->$age_field, 27*3, 'Fetched age expression is correct.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
