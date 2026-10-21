# DatabaseInsertLOBTestCase::testInsertOneBlob()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 740–748 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L740-L748)
- **Class:** [DatabaseInsertLOBTestCase](../DatabaseInsertLOBTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testInsertOneBlob()
```

## Documentation

```text
Test that we can insert a single blob field successfully.
```

## Code

```php
  function testInsertOneBlob() {
    $data = "This is\000a test.";
    $this->assertTrue(strlen($data) === 15, 'Test data contains a NULL.');
    $id = db_insert('test_one_blob')
      ->fields(array('blob1' => $data))
      ->execute();
    $r = db_query('SELECT * FROM {test_one_blob} WHERE id = :id', array(':id' => $id))->fetchAssoc();
    $this->assertTrue($r['blob1'] === $data, format_string('Can insert a blob: id @id, @data.', array('@id' => $id, '@data' => serialize($r))));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
