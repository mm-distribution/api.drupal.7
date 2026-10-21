# DatabaseUpdateTestCase::testMultiGTUpdate()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 884–893 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L884-L893)
- **Class:** [DatabaseUpdateTestCase](../DatabaseUpdateTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testMultiGTUpdate()
```

## Documentation

```text
Confirm that we can update a multiple records with a non-equality condition.
```

## Code

```php
  function testMultiGTUpdate() {
    $num_updated = db_update('test')
      ->fields(array('job' => 'Musician'))
      ->condition('age', 26, '>')
      ->execute();
    $this->assertIdentical($num_updated, 2, 'Updated 2 records.');

    $num_matches = db_query('SELECT COUNT(*) FROM {test} WHERE job = :job', array(':job' => 'Musician'))->fetchField();
    $this->assertIdentical($num_matches, '2', 'Updated fields successfully.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
