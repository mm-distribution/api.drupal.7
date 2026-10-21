# DatabaseInsertTestCase::testInsertLastInsertID()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 665–674 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L665-L674)
- **Class:** [DatabaseInsertTestCase](../DatabaseInsertTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testInsertLastInsertID()
```

## Documentation

```text
Test that inserts return the proper auto-increment ID.
```

## Code

```php
  function testInsertLastInsertID() {
    $id = db_insert('test')
      ->fields(array(
        'name' => 'Larry',
        'age' => '30',
      ))
      ->execute();

    $this->assertIdentical($id, '5', 'Auto-increment ID returned successfully.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
