# FileDeleteTest::testInUse()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1775–1797 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1775-L1797)
- **Class:** [FileDeleteTest](../FileDeleteTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testInUse()
```

## Documentation

```text
Tries deleting a file that is in use.
```

## Code

```php
  function testInUse() {
    $file = $this->createFile();
    file_usage_add($file, 'testing', 'test', 1);
    file_usage_add($file, 'testing', 'test', 1);

    file_usage_delete($file, 'testing', 'test', 1);
    file_delete($file);
    $usage = file_usage_list($file);
    $this->assertEqual($usage['testing']['test'], array(1 => 1), 'Test file is still in use.');
    $this->assertTrue(file_exists($file->uri), 'File still exists on the disk.');
    $this->assertTrue(file_load($file->fid), 'File still exists in the database.');

    // Clear out the call to hook_file_load().
    file_test_reset();

    file_usage_delete($file, 'testing', 'test', 1);
    file_delete($file);
    $usage = file_usage_list($file);
    $this->assertFileHooksCalled(array('delete'));
    $this->assertTrue(empty($usage), 'File usage data was removed.');
    $this->assertFalse(file_exists($file->uri), 'File has been deleted after its last usage was removed.');
    $this->assertFalse(file_load($file->fid), 'File was removed from the database.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
