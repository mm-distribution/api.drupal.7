# FileFieldTestCase::assertFileExists()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 182–185 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L182-L185)
- **Class:** [FileFieldTestCase](../FileFieldTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
function assertFileExists($file, $message = NULL)
```

## Documentation

```text
Asserts that a file exists physically on disk.
```

## Code

```php
  function assertFileExists($file, $message = NULL) {
    $message = isset($message) ? $message : format_string('File %file exists on the disk.', array('%file' => $file->uri));
    $this->assertTrue(is_file($file->uri), $message);
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
