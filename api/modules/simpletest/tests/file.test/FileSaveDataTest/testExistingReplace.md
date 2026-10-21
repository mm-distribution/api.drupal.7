# FileSaveDataTest::testExistingReplace()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 2522–2544 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L2522-L2544)
- **Class:** [FileSaveDataTest](../FileSaveDataTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testExistingReplace()
```

## Documentation

```text
Test file_save_data() when replacing an existing file.
```

## Code

```php
  function testExistingReplace() {
    // Setup a file to overwrite.
    $existing = $this->createFile();
    $contents = $this->randomName(8);

    $result = file_save_data($contents, $existing->uri, FILE_EXISTS_REPLACE);
    $this->assertTrue($result, 'File saved successfully.');

    $this->assertEqual('public', file_uri_scheme($result->uri), "File was placed in Drupal's files directory.");
    $this->assertEqual($result->filename, $existing->filename, 'Filename was set to the basename of the existing file, rather than preserving the original name.');
    $this->assertEqual($contents, file_get_contents($result->uri), 'Contents of the file are correct.');
    $this->assertEqual($result->filemime, 'application/octet-stream', 'A MIME type was set.');
    $this->assertEqual($result->status, FILE_STATUS_PERMANENT, "The file's status was set to permanent.");

    // Check that the correct hooks were called.
    $this->assertFileHooksCalled(array('load', 'update'));

    // Verify that the existing file was re-used.
    $this->assertSameFile($existing, $result);

    // Verify that what was returned is what's in the database.
    $this->assertFileUnchanged($result, file_load($result->fid, TRUE));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
