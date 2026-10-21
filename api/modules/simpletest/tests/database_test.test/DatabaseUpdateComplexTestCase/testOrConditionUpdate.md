# DatabaseUpdateComplexTestCase::testOrConditionUpdate()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 977–989 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L977-L989)
- **Class:** [DatabaseUpdateComplexTestCase](../DatabaseUpdateComplexTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testOrConditionUpdate()
```

## Documentation

```text
Test updates with OR conditionals.
```

## Code

```php
  function testOrConditionUpdate() {
    $update = db_update('test')
      ->fields(array('job' => 'Musician'))
      ->condition(db_or()
        ->condition('name', 'John')
        ->condition('name', 'Paul')
      );
    $num_updated = $update->execute();
    $this->assertIdentical($num_updated, 2, 'Updated 2 records.');

    $num_matches = db_query('SELECT COUNT(*) FROM {test} WHERE job = :job', array(':job' => 'Musician'))->fetchField();
    $this->assertIdentical($num_matches, '2', 'Updated fields successfully.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
