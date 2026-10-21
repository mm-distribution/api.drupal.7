# DatabaseDeleteTruncateTestCase::testSimpleDelete()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 1187–1197 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L1187-L1197)
- **Class:** [DatabaseDeleteTruncateTestCase](../DatabaseDeleteTruncateTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testSimpleDelete()
```

## Documentation

```text
Confirm that we can delete a single record successfully.
```

## Code

```php
  function testSimpleDelete() {
    $num_records_before = db_query('SELECT COUNT(*) FROM {test}')->fetchField();

    $num_deleted = db_delete('test')
      ->condition('id', 1)
      ->execute();
    $this->assertIdentical($num_deleted, 1, 'Deleted 1 record.');

    $num_records_after = db_query('SELECT COUNT(*) FROM {test}')->fetchField();
    $this->assertEqual($num_records_before, $num_records_after + $num_deleted, 'Deletion adds up.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
