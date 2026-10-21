# DatabaseUpdateComplexTestCase::testLikeConditionUpdate()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 1038–1047 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L1038-L1047)
- **Class:** [DatabaseUpdateComplexTestCase](../DatabaseUpdateComplexTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testLikeConditionUpdate()
```

## Documentation

```text
Test LIKE conditionals.
```

## Code

```php
  function testLikeConditionUpdate() {
    $num_updated = db_update('test')
      ->fields(array('job' => 'Musician'))
      ->condition('name', '%ge%', 'LIKE')
      ->execute();
    $this->assertIdentical($num_updated, 1, 'Updated 1 record.');

    $num_matches = db_query('SELECT COUNT(*) FROM {test} WHERE job = :job', array(':job' => 'Musician'))->fetchField();
    $this->assertIdentical($num_matches, '1', 'Updated fields successfully.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
