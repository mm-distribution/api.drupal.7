# FileFieldTestCase::getTestFile()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 32–40 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L32-L40)
- **Class:** [FileFieldTestCase](../FileFieldTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
function getTestFile($type_name, $size = NULL)
```

## Documentation

```text
Retrieves a sample file of the specified type.
```

## Code

```php
  function getTestFile($type_name, $size = NULL) {
    // Get a file to upload.
    $file = current($this->drupalGetTestFiles($type_name, $size));

    // Add a filesize property to files as would be read by file_load().
    $file->filesize = filesize($file->uri);

    return $file;
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
