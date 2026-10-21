# DatabaseUpdateTestCase::testSimpleNullUpdate()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 855–865 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L855-L865)
- **Class:** [DatabaseUpdateTestCase](../DatabaseUpdateTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testSimpleNullUpdate()
```

## Documentation

```text
Confirm updating to NULL.
```

## Code

```php
  function testSimpleNullUpdate() {
    $this->ensureSampleDataNull();
    $num_updated = db_update('test_null')
      ->fields(array('age' => NULL))
      ->condition('name', 'Kermit')
      ->execute();
    $this->assertIdentical($num_updated, 1, 'Updated 1 record.');

    $saved_age = db_query('SELECT age FROM {test_null} WHERE name = :name', array(':name' => 'Kermit'))->fetchField();
    $this->assertNull($saved_age, 'Updated name successfully.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
