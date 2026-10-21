# DatabaseSelectTestCase::testSimpleSelectExpressionMultiple()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 1575–1592 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L1575-L1592)
- **Class:** [DatabaseSelectTestCase](../DatabaseSelectTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testSimpleSelectExpressionMultiple()
```

## Documentation

```text
Test SELECT statements with multiple expressions.
```

## Code

```php
  function testSimpleSelectExpressionMultiple() {
    $query = db_select('test');
    $name_field = $query->addField('test', 'name');
    $age_double_field = $query->addExpression("age*2");
    $age_triple_field = $query->addExpression("age*3");
    $query->condition('age', 27);
    $result = $query->execute();

    // Check that the aliases are being created the way we want.
    $this->assertEqual($age_double_field, 'expression', 'Double age field alias is correct.');
    $this->assertEqual($age_triple_field, 'expression_2', 'Triple age field alias is correct.');

    // Ensure that we got the right record.
    $record = $result->fetch();
    $this->assertEqual($record->$name_field, 'George', 'Fetched name is correct.');
    $this->assertEqual($record->$age_double_field, 27*2, 'Fetched double age expression is correct.');
    $this->assertEqual($record->$age_triple_field, 27*3, 'Fetched triple age expression is correct.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
