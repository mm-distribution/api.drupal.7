# DatabaseUpdateTestCase::testWhereAndConditionUpdate()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 912–922 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L912-L922)
- **Class:** [DatabaseUpdateTestCase](../DatabaseUpdateTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testWhereAndConditionUpdate()
```

## Documentation

```text
Confirm that we can stack condition and where calls.
```

## Code

```php
  function testWhereAndConditionUpdate() {
    $update = db_update('test')
      ->fields(array('job' => 'Musician'))
      ->where('age > :age', array(':age' => 26))
      ->condition('name', 'Ringo');
    $num_updated = $update->execute();
    $this->assertIdentical($num_updated, 1, 'Updated 1 record.');

    $num_matches = db_query('SELECT COUNT(*) FROM {test} WHERE job = :job', array(':job' => 'Musician'))->fetchField();
    $this->assertIdentical($num_matches, '1', 'Updated fields successfully.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
