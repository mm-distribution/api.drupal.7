# DatabaseInsertTestCase::testInsertFieldOnlyDefinintion()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 645–660 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L645-L660)
- **Class:** [DatabaseInsertTestCase](../DatabaseInsertTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testInsertFieldOnlyDefinintion()
```

## Documentation

```text
Test that we can specify fields without values and specify values later.
```

## Code

```php
  function testInsertFieldOnlyDefinintion() {
    // This is useful for importers, when we want to create a query and define
    // its fields once, then loop over a multi-insert execution.
    db_insert('test')
      ->fields(array('name', 'age'))
      ->values(array('Larry', '30'))
      ->values(array('Curly', '31'))
      ->values(array('Moe', '32'))
      ->execute();
    $saved_age = db_query('SELECT age FROM {test} WHERE name = :name', array(':name' => 'Larry'))->fetchField();
    $this->assertIdentical($saved_age, '30', 'Can retrieve after inserting.');
    $saved_age = db_query('SELECT age FROM {test} WHERE name = :name', array(':name' => 'Curly'))->fetchField();
    $this->assertIdentical($saved_age, '31', 'Can retrieve after inserting.');
    $saved_age = db_query('SELECT age FROM {test} WHERE name = :name', array(':name' => 'Moe'))->fetchField();
    $this->assertIdentical($saved_age, '32', 'Can retrieve after inserting.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
