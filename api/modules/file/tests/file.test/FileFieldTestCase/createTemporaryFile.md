# FileFieldTestCase::createTemporaryFile()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 233–244 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L233-L244)
- **Class:** [FileFieldTestCase](../FileFieldTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
function createTemporaryFile($data, $uid = NULL)
```

## Documentation

```text
Creates a temporary file, for a specific user.

@param string $data
  A string containing the contents of the file.
@param int $uid
  The user ID of the file owner.

@return object
  A file object, or FALSE on error.
```

## Code

```php
  function createTemporaryFile($data, $uid = NULL) {
    $file = file_save_data($data, NULL, NULL);

    if ($file) {
      $file->uid = isset($uid) ? $uid : $this->admin_user->uid;
      // Change the file status to be temporary.
      $file->status = NULL;
      return file_save($file);
    }

    return $file;
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
