# file_validate_size()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 1833–1847 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L1833-L1847)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_validate_size(stdClass $file, $file_limit = 0, $user_limit = 0)
```

## Documentation

```text
Checks that the file's size is below certain limits.

@param $file
  A Drupal file object.
@param $file_limit
  An integer specifying the maximum file size in bytes. Zero indicates that
  no limit should be enforced.
@param $user_limit
  An integer specifying the maximum number of bytes the user is allowed.
  Zero indicates that no limit should be enforced.

@return
  An array. If the file size exceeds limits, it will contain an error
  message.

@see hook_file_validate()
```

## Code

```php
function file_validate_size(stdClass $file, $file_limit = 0, $user_limit = 0) {
  global $user;
  $errors = array();

  if ($file_limit && $file->filesize > $file_limit) {
    $errors[] = t('The file is %filesize exceeding the maximum file size of %maxsize.', array('%filesize' => format_size($file->filesize), '%maxsize' => format_size($file_limit)));
  }

  // Save a query by only calling file_space_used() when a limit is provided.
  if ($user_limit && (file_space_used($user->uid) + $file->filesize) > $user_limit) {
    $errors[] = t('The file is %filesize which would exceed your disk quota of %quota.', array('%filesize' => format_size($file->filesize), '%quota' => format_size($user_limit)));
  }

  return $errors;
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
