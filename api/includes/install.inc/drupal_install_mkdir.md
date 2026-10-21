# drupal_install_mkdir()

- **Type:** Function
- **File:** [`includes/install.inc`](_file.md), lines 923–948 · [local source](../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L923-L948)

## Signature

```php
function drupal_install_mkdir($file, $mask, $message = TRUE)
```

## Documentation

```text
Creates a directory with the specified permissions.

@param $file
 The name of the directory to create;
@param $mask
 The permissions of the directory to create.
@param $message
 (optional) Whether to output messages. Defaults to TRUE.

@return
 TRUE/FALSE whether or not the directory was successfully created.
```

## Code

```php
function drupal_install_mkdir($file, $mask, $message = TRUE) {
  $mod = 0;
  $masks = array(FILE_READABLE, FILE_WRITABLE, FILE_EXECUTABLE, FILE_NOT_READABLE, FILE_NOT_WRITABLE, FILE_NOT_EXECUTABLE);
  foreach ($masks as $m) {
    if ($mask & $m) {
      switch ($m) {
        case FILE_READABLE:
          $mod |= 0444;
          break;
        case FILE_WRITABLE:
          $mod |= 0222;
          break;
        case FILE_EXECUTABLE:
          $mod |= 0111;
          break;
      }
    }
  }

  if (@drupal_mkdir($file, $mod)) {
    return TRUE;
  }
  else {
    return FALSE;
  }
}
```

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
