# FileFieldAnonymousSubmission::getTestImage()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 1936–1944 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L1936-L1944)
- **Class:** [FileFieldAnonymousSubmission](../FileFieldAnonymousSubmission.md)
- **Module/theme:** file_module_test

## Signature

```php
function getTestImage()
```

## Documentation

```text
Generates a test image.

@return stdClass
  A file object.
```

## Code

```php
  function getTestImage() {
    // Get a file to upload.
    $file = current($this->drupalGetTestFiles('image'));

    // Add a filesize property to files as would be read by file_load().
    $file->filesize = filesize($file->uri);

    return $file;
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
