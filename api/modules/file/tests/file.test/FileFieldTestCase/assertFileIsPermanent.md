# FileFieldTestCase::assertFileIsPermanent()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 217–220 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L217-L220)
- **Class:** [FileFieldTestCase](../FileFieldTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
function assertFileIsPermanent($file, $message = NULL)
```

## Documentation

```text
Asserts that a file's status is set to permanent in the database.
```

## Code

```php
  function assertFileIsPermanent($file, $message = NULL) {
    $message = isset($message) ? $message : format_string('File %file is permanent.', array('%file' => $file->uri));
    $this->assertTrue($file->status == FILE_STATUS_PERMANENT, $message);
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
