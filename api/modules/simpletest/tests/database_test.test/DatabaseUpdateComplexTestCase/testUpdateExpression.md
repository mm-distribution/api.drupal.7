# DatabaseUpdateComplexTestCase::testUpdateExpression()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 1052–1070 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L1052-L1070)
- **Class:** [DatabaseUpdateComplexTestCase](../DatabaseUpdateComplexTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testUpdateExpression()
```

## Documentation

```text
Test update with expression values.
```

## Code

```php
  function testUpdateExpression() {
    $before_age = db_query('SELECT age FROM {test} WHERE name = :name', array(':name' => 'Ringo'))->fetchField();
    $GLOBALS['larry_test'] = 1;
    $num_updated = db_update('test')
      ->condition('name', 'Ringo')
      ->fields(array('job' => 'Musician'))
      ->expression('age', 'age + :age', array(':age' => 4))
      ->execute();
    $this->assertIdentical($num_updated, 1, 'Updated 1 record.');

    $num_matches = db_query('SELECT COUNT(*) FROM {test} WHERE job = :job', array(':job' => 'Musician'))->fetchField();
    $this->assertIdentical($num_matches, '1', 'Updated fields successfully.');

    $person = db_query('SELECT * FROM {test} WHERE name = :name', array(':name' => 'Ringo'))->fetch();
    $this->assertEqual($person->name, 'Ringo', 'Name set correctly.');
    $this->assertEqual($person->age, $before_age + 4, 'Age set correctly.');
    $this->assertEqual($person->job, 'Musician', 'Job set correctly.');
    $GLOBALS['larry_test'] = 0;
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
