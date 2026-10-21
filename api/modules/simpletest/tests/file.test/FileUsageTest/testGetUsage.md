# FileUsageTest::testGetUsage()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 2275–2303 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L2275-L2303)
- **Class:** [FileUsageTest](../FileUsageTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testGetUsage()
```

## Documentation

```text
Tests file_usage_list().
```

## Code

```php
  function testGetUsage() {
    $file = $this->createFile();
    db_insert('file_usage')
      ->fields(array(
        'fid' => $file->fid,
        'module' => 'testing',
        'type' => 'foo',
        'id' => 1,
        'count' => 1
      ))
      ->execute();
    db_insert('file_usage')
      ->fields(array(
        'fid' => $file->fid,
        'module' => 'testing',
        'type' => 'bar',
        'id' => 2,
        'count' => 2
      ))
      ->execute();

    $usage = file_usage_list($file);

    $this->assertEqual(count($usage['testing']), 2, 'Returned the correct number of items.');
    $this->assertTrue(isset($usage['testing']['foo'][1]), 'Returned the correct id.');
    $this->assertTrue(isset($usage['testing']['bar'][2]), 'Returned the correct id.');
    $this->assertEqual($usage['testing']['foo'][1], 1, 'Returned the correct count.');
    $this->assertEqual($usage['testing']['bar'][2], 2, 'Returned the correct count.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
