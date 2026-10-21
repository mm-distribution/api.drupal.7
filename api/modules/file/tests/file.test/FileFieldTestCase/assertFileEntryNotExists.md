# FileFieldTestCase::assertFileEntryNotExists()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 208–212 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L208-L212)
- **Class:** [FileFieldTestCase](../FileFieldTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
function assertFileEntryNotExists($file, $message)
```

## Documentation

```text
Asserts that a file does not exist in the database.
```

## Code

```php
  function assertFileEntryNotExists($file, $message) {
    entity_get_controller('file')->resetCache();
    $message = isset($message) ? $message : format_string('File %file exists in database at the correct path.', array('%file' => $file->uri));
    $this->assertFalse(file_load($file->fid), $message);
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
