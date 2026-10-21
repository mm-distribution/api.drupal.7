# drupal_verify_install_file()

- **Type:** Function
- **File:** [`includes/install.inc`](_file.md), lines 840–908 · [local source](../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L840-L908)

## Signature

```php
function drupal_verify_install_file($file, $mask = NULL, $type = 'file', $autofix = TRUE)
```

## Documentation

```text
Verifies the state of the specified file.

@param $file
  The file to check for.
@param $mask
  An optional bitmask created from various FILE_* constants.
@param $type
  The type of file. Can be file (default), dir, or link.
@param bool $autofix
  (optional) Determines whether to attempt fixing the permissions according
  to the provided $mask. Defaults to TRUE.

@return
  TRUE on success or FALSE on failure. A message is set for the latter.
```

## Code

```php
function drupal_verify_install_file($file, $mask = NULL, $type = 'file', $autofix = TRUE) {
  $return = TRUE;
  // Check for files that shouldn't be there.
  if (isset($mask) && ($mask & FILE_NOT_EXIST) && file_exists($file)) {
    return FALSE;
  }
  // Verify that the file is the type of file it is supposed to be.
  if (isset($type) && file_exists($file)) {
    $check = 'is_' . $type;
    if (!function_exists($check) || !$check($file)) {
      $return = FALSE;
    }
  }

  // Verify file permissions.
  if (isset($mask)) {
    $masks = array(FILE_EXIST, FILE_READABLE, FILE_WRITABLE, FILE_EXECUTABLE, FILE_NOT_READABLE, FILE_NOT_WRITABLE, FILE_NOT_EXECUTABLE);
    foreach ($masks as $current_mask) {
      if ($mask & $current_mask) {
        switch ($current_mask) {
          case FILE_EXIST:
            if (!file_exists($file)) {
              if ($type == 'dir' && $autofix) {
                drupal_install_mkdir($file, $mask);
              }
              if (!file_exists($file)) {
                $return = FALSE;
              }
            }
            break;
          case FILE_READABLE:
            if (!is_readable($file)) {
              $return = FALSE;
            }
            break;
          case FILE_WRITABLE:
            if (!is_writable($file)) {
              $return = FALSE;
            }
            break;
          case FILE_EXECUTABLE:
            if (!is_executable($file)) {
              $return = FALSE;
            }
            break;
          case FILE_NOT_READABLE:
            if (is_readable($file)) {
              $return = FALSE;
            }
            break;
          case FILE_NOT_WRITABLE:
            if (is_writable($file)) {
              $return = FALSE;
            }
            break;
          case FILE_NOT_EXECUTABLE:
            if (is_executable($file)) {
              $return = FALSE;
            }
            break;
        }
      }
    }
  }
  if (!$return && $autofix) {
    return drupal_install_fix_file($file, $mask);
  }
  return $return;
}
```

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
