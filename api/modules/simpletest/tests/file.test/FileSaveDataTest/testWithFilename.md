# FileSaveDataTest::testWithFilename()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 2469–2489 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L2469-L2489)
- **Class:** [FileSaveDataTest](../FileSaveDataTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testWithFilename()
```

## Documentation

```text
Test the file_save_data() function when a filename is provided.
```

## Code

```php
  function testWithFilename() {
    $contents = $this->randomName(8);

    // Using filename with non-latin characters.
    $filename = 'Текстовый файл.txt';

    $result = file_save_data($contents, 'public://' . $filename);
    $this->assertTrue($result, 'Unnamed file saved correctly.');

    $this->assertEqual('public', file_uri_scheme($result->uri), "File was placed in Drupal's files directory.");
    $this->assertEqual($filename, drupal_basename($result->uri), 'File was named correctly.');
    $this->assertEqual($contents, file_get_contents($result->uri), 'Contents of the file are correct.');
    $this->assertEqual($result->filemime, 'text/plain', 'A MIME type was set.');
    $this->assertEqual($result->status, FILE_STATUS_PERMANENT, "The file's status was set to permanent.");

    // Check that the correct hooks were called.
    $this->assertFileHooksCalled(array('insert'));

    // Verify that what was returned is what's in the database.
    $this->assertFileUnchanged($result, file_load($result->fid, TRUE));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
