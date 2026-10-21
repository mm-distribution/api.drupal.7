# FileTestCase::createFile()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 201–232 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L201-L232)
- **Class:** [FileTestCase](../FileTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function createFile($filepath = NULL, $contents = NULL, $scheme = NULL)
```

## Documentation

```text
Create a file and save it to the files table and assert that it occurs
correctly.

@param $filepath
  Optional string specifying the file path. If none is provided then a
  randomly named file will be created in the site's files directory.
@param $contents
  Optional contents to save into the file. If a NULL value is provided an
  arbitrary string will be used.
@param $scheme
  Optional string indicating the stream scheme to use. Drupal core includes
  public, private, and temporary. The public wrapper is the default.
@return
  File object.
```

## Code

```php
  function createFile($filepath = NULL, $contents = NULL, $scheme = NULL) {
    if (!isset($filepath)) {
      // Prefix with non-latin characters to ensure that all file-related
      // tests work with international filenames.
      $filepath = 'Файл для тестирования ' . $this->randomName();
    }
    if (!isset($scheme)) {
      $scheme = file_default_scheme();
    }
    $filepath = $scheme . '://' . $filepath;

    if (!isset($contents)) {
      $contents = "file_put_contents() doesn't seem to appreciate empty strings so let's put in some data.";
    }

    file_put_contents($filepath, $contents);
    $this->assertTrue(is_file($filepath), 'The test file exists on the disk.', 'Create test file');

    $file = new stdClass();
    $file->uri = $filepath;
    $file->filename = drupal_basename($file->uri);
    $file->filemime = 'text/plain';
    $file->uid = 1;
    $file->timestamp = REQUEST_TIME;
    $file->filesize = filesize($file->uri);
    $file->status = 0;
    // Write the record directly rather than calling file_save() so we don't
    // invoke the hooks.
    $this->assertNotIdentical(drupal_write_record('file_managed', $file), FALSE, 'The file was added to the database.', 'Create test file');

    return $file;
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
