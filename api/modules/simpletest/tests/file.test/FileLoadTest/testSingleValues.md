# FileLoadTest::testSingleValues()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 2149–2162 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L2149-L2162)
- **Class:** [FileLoadTest](../FileLoadTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testSingleValues()
```

## Documentation

```text
Load a single file and ensure that the correct values are returned.
```

## Code

```php
  function testSingleValues() {
    // Create a new file object from scratch so we know the values.
    $file = $this->createFile('druplicon.txt', NULL, 'public');

    $by_fid_file = file_load($file->fid);
    $this->assertFileHookCalled('load');
    $this->assertTrue(is_object($by_fid_file), 'file_load() returned an object.');
    $this->assertEqual($by_fid_file->fid, $file->fid, 'Loading by fid got the same fid.', 'File');
    $this->assertEqual($by_fid_file->uri, $file->uri, 'Loading by fid got the correct filepath.', 'File');
    $this->assertEqual($by_fid_file->filename, $file->filename, 'Loading by fid got the correct filename.', 'File');
    $this->assertEqual($by_fid_file->filemime, $file->filemime, 'Loading by fid got the correct MIME type.', 'File');
    $this->assertEqual($by_fid_file->status, $file->status, 'Loading by fid got the correct status.', 'File');
    $this->assertTrue($by_fid_file->file_test['loaded'], 'file_test_file_load() was able to modify the file during load.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
