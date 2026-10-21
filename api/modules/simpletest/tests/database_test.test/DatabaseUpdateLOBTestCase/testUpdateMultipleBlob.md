# DatabaseUpdateLOBTestCase::testUpdateMultipleBlob()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 1124–1139 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L1124-L1139)
- **Class:** [DatabaseUpdateLOBTestCase](../DatabaseUpdateLOBTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testUpdateMultipleBlob()
```

## Documentation

```text
Confirm that we can update two blob columns in the same table.
```

## Code

```php
  function testUpdateMultipleBlob() {
    $id = db_insert('test_two_blobs')
      ->fields(array(
        'blob1' => 'This is',
        'blob2' => 'a test',
      ))
      ->execute();

    db_update('test_two_blobs')
      ->condition('id', $id)
      ->fields(array('blob1' => 'and so', 'blob2' => 'is this'))
      ->execute();

    $r = db_query('SELECT * FROM {test_two_blobs} WHERE id = :id', array(':id' => $id))->fetchAssoc();
    $this->assertTrue($r['blob1'] === 'and so' && $r['blob2'] === 'is this', 'Can update multiple blobs per row.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
