# DatabaseInsertLOBTestCase::testInsertMultipleBlob()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 753–762 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L753-L762)
- **Class:** [DatabaseInsertLOBTestCase](../DatabaseInsertLOBTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testInsertMultipleBlob()
```

## Documentation

```text
Test that we can insert multiple blob fields in the same query.
```

## Code

```php
  function testInsertMultipleBlob() {
    $id = db_insert('test_two_blobs')
      ->fields(array(
        'blob1' => 'This is',
        'blob2' => 'a test',
      ))
      ->execute();
    $r = db_query('SELECT * FROM {test_two_blobs} WHERE id = :id', array(':id' => $id))->fetchAssoc();
    $this->assertTrue($r['blob1'] === 'This is' && $r['blob2'] === 'a test', 'Can insert multiple blobs per row.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
