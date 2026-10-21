# FileFieldTestCase::assertFileEntryExists()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 190–195 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L190-L195)
- **Class:** [FileFieldTestCase](../FileFieldTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
function assertFileEntryExists($file, $message = NULL)
```

## Documentation

```text
Asserts that a file exists in the database.
```

## Code

```php
  function assertFileEntryExists($file, $message = NULL) {
    entity_get_controller('file')->resetCache();
    $db_file = file_load($file->fid);
    $message = isset($message) ? $message : format_string('File %file exists in database at the correct path.', array('%file' => $file->uri));
    $this->assertEqual($db_file->uri, $file->uri, $message);
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
