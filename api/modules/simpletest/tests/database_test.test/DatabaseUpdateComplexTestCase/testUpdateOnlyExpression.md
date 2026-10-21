# DatabaseUpdateComplexTestCase::testUpdateOnlyExpression()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 1075–1085 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L1075-L1085)
- **Class:** [DatabaseUpdateComplexTestCase](../DatabaseUpdateComplexTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testUpdateOnlyExpression()
```

## Documentation

```text
Test update with only expression values.
```

## Code

```php
  function testUpdateOnlyExpression() {
    $before_age = db_query('SELECT age FROM {test} WHERE name = :name', array(':name' => 'Ringo'))->fetchField();
    $num_updated = db_update('test')
      ->condition('name', 'Ringo')
      ->expression('age', 'age + :age', array(':age' => 4))
      ->execute();
    $this->assertIdentical($num_updated, 1, 'Updated 1 record.');

    $after_age = db_query('SELECT age FROM {test} WHERE name = :name', array(':name' => 'Ringo'))->fetchField();
    $this->assertEqual($before_age + 4, $after_age, 'Age updated correctly');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
