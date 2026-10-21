# FileFieldTestCase::assertFileNotExists()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 200–203 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L200-L203)
- **Class:** [FileFieldTestCase](../FileFieldTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
function assertFileNotExists($file, $message = NULL)
```

## Documentation

```text
Asserts that a file does not exist on disk.
```

## Code

```php
  function assertFileNotExists($file, $message = NULL) {
    $message = isset($message) ? $message : format_string('File %file exists on the disk.', array('%file' => $file->uri));
    $this->assertFalse(is_file($file->uri), $message);
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
