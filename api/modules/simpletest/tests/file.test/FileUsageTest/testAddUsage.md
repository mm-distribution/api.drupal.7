# FileUsageTest::testAddUsage()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 2308–2328 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L2308-L2328)
- **Class:** [FileUsageTest](../FileUsageTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testAddUsage()
```

## Documentation

```text
Tests file_usage_add().
```

## Code

```php
  function testAddUsage() {
    $file = $this->createFile();
    file_usage_add($file, 'testing', 'foo', 1);
    // Add the file twice to ensure that the count is incremented rather than
    // creating additional records.
    file_usage_add($file, 'testing', 'bar', 2);
    file_usage_add($file, 'testing', 'bar', 2);

    $usage = db_select('file_usage', 'f')
      ->fields('f')
      ->condition('f.fid', $file->fid)
      ->execute()
      ->fetchAllAssoc('id');
    $this->assertEqual(count($usage), 2, 'Created two records');
    $this->assertEqual($usage[1]->module, 'testing', 'Correct module');
    $this->assertEqual($usage[2]->module, 'testing', 'Correct module');
    $this->assertEqual($usage[1]->type, 'foo', 'Correct type');
    $this->assertEqual($usage[2]->type, 'bar', 'Correct type');
    $this->assertEqual($usage[1]->count, 1, 'Correct count');
    $this->assertEqual($usage[2]->count, 2, 'Correct count');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
