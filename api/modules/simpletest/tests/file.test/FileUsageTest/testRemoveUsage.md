# FileUsageTest::testRemoveUsage()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 2333–2371 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L2333-L2371)
- **Class:** [FileUsageTest](../FileUsageTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testRemoveUsage()
```

## Documentation

```text
Tests file_usage_delete().
```

## Code

```php
  function testRemoveUsage() {
    $file = $this->createFile();
    db_insert('file_usage')
      ->fields(array(
        'fid' => $file->fid,
        'module' => 'testing',
        'type' => 'bar',
        'id' => 2,
        'count' => 3,
      ))
      ->execute();

    // Normal decrement.
    file_usage_delete($file, 'testing', 'bar', 2);
    $count = db_select('file_usage', 'f')
      ->fields('f', array('count'))
      ->condition('f.fid', $file->fid)
      ->execute()
      ->fetchField();
    $this->assertEqual(2, $count, 'The count was decremented correctly.');

    // Multiple decrement and removal.
    file_usage_delete($file, 'testing', 'bar', 2, 2);
    $count = db_select('file_usage', 'f')
      ->fields('f', array('count'))
      ->condition('f.fid', $file->fid)
      ->execute()
      ->fetchField();
    $this->assertIdentical(FALSE, $count, 'The count was removed entirely when empty.');

    // Non-existent decrement.
    file_usage_delete($file, 'testing', 'bar', 2);
    $count = db_select('file_usage', 'f')
      ->fields('f', array('count'))
      ->condition('f.fid', $file->fid)
      ->execute()
      ->fetchField();
    $this->assertIdentical(FALSE, $count, 'Decrementing non-exist record complete.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
