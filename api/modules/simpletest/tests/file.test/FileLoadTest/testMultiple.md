# FileLoadTest::testMultiple()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 2167–2188 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L2167-L2188)
- **Class:** [FileLoadTest](../FileLoadTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testMultiple()
```

## Documentation

```text
This will test loading file data from the database.
```

## Code

```php
  function testMultiple() {
    // Create a new file object.
    $file = $this->createFile('druplicon.txt', NULL, 'public');

    // Load by path.
    file_test_reset();
    $by_path_files = file_load_multiple(array(), array('uri' => $file->uri));
    $this->assertFileHookCalled('load');
    $this->assertEqual(1, count($by_path_files), 'file_load_multiple() returned an array of the correct size.');
    $by_path_file = reset($by_path_files);
    $this->assertTrue($by_path_file->file_test['loaded'], 'file_test_file_load() was able to modify the file during load.');
    $this->assertEqual($by_path_file->fid, $file->fid, 'Loading by filepath got the correct fid.', 'File');

    // Load by fid.
    file_test_reset();
    $by_fid_files = file_load_multiple(array($file->fid), array());
    $this->assertFileHookCalled('load');
    $this->assertEqual(1, count($by_fid_files), 'file_load_multiple() returned an array of the correct size.');
    $by_fid_file = reset($by_fid_files);
    $this->assertTrue($by_fid_file->file_test['loaded'], 'file_test_file_load() was able to modify the file during load.');
    $this->assertEqual($by_fid_file->uri, $file->uri, 'Loading by fid got the correct filepath.', 'File');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
