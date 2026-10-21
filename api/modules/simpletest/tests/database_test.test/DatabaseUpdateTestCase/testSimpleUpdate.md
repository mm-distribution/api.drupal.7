# DatabaseUpdateTestCase::testSimpleUpdate()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 841–850 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L841-L850)
- **Class:** [DatabaseUpdateTestCase](../DatabaseUpdateTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testSimpleUpdate()
```

## Documentation

```text
Confirm that we can update a single record successfully.
```

## Code

```php
  function testSimpleUpdate() {
    $num_updated = db_update('test')
      ->fields(array('name' => 'Tiffany'))
      ->condition('id', 1)
      ->execute();
    $this->assertIdentical($num_updated, 1, 'Updated 1 record.');

    $saved_name = db_query('SELECT name FROM {test} WHERE id = :id', array(':id' => 1))->fetchField();
    $this->assertIdentical($saved_name, 'Tiffany', 'Updated name successfully.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
