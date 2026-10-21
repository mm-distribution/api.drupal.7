# FileSaveDataTest::testWithoutFilename()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 2447–2464 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L2447-L2464)
- **Class:** [FileSaveDataTest](../FileSaveDataTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testWithoutFilename()
```

## Documentation

```text
Test the file_save_data() function when no filename is provided.
```

## Code

```php
  function testWithoutFilename() {
    $contents = $this->randomName(8);

    $result = file_save_data($contents);
    $this->assertTrue($result, 'Unnamed file saved correctly.');

    $this->assertEqual(file_default_scheme(), file_uri_scheme($result->uri), "File was placed in Drupal's files directory.");
    $this->assertEqual($result->filename, drupal_basename($result->uri), "Filename was set to the file's basename.");
    $this->assertEqual($contents, file_get_contents($result->uri), 'Contents of the file are correct.');
    $this->assertEqual($result->filemime, 'application/octet-stream', 'A MIME type was set.');
    $this->assertEqual($result->status, FILE_STATUS_PERMANENT, "The file's status was set to permanent.");

    // Check that the correct hooks were called.
    $this->assertFileHooksCalled(array('insert'));

    // Verify that what was returned is what's in the database.
    $this->assertFileUnchanged($result, file_load($result->fid, TRUE));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
