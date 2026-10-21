# FileSaveDataTest::testExistingRename()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 2494–2517 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L2494-L2517)
- **Class:** [FileSaveDataTest](../FileSaveDataTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testExistingRename()
```

## Documentation

```text
Test file_save_data() when renaming around an existing file.
```

## Code

```php
  function testExistingRename() {
    // Setup a file to overwrite.
    $existing = $this->createFile();
    $contents = $this->randomName(8);

    $result = file_save_data($contents, $existing->uri, FILE_EXISTS_RENAME);
    $this->assertTrue($result, 'File saved successfully.');

    $this->assertEqual('public', file_uri_scheme($result->uri), "File was placed in Drupal's files directory.");
    $this->assertEqual($result->filename, $existing->filename, 'Filename was set to the basename of the source, rather than that of the renamed file.');
    $this->assertEqual($contents, file_get_contents($result->uri), 'Contents of the file are correct.');
    $this->assertEqual($result->filemime, 'application/octet-stream', 'A MIME type was set.');
    $this->assertEqual($result->status, FILE_STATUS_PERMANENT, "The file's status was set to permanent.");

    // Check that the correct hooks were called.
    $this->assertFileHooksCalled(array('insert'));

    // Ensure that the existing file wasn't overwritten.
    $this->assertDifferentFile($existing, $result);
    $this->assertFileUnchanged($existing, file_load($existing->fid, TRUE));

    // Verify that was returned is what's in the database.
    $this->assertFileUnchanged($result, file_load($result->fid, TRUE));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
