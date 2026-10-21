# drupal_install_fix_file()

- **Type:** Function
- **File:** [`includes/install.inc`](_file.md), lines 972–1031 · [local source](../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L972-L1031)

## Signature

```php
function drupal_install_fix_file($file, $mask, $message = TRUE)
```

## Documentation

```text
Attempts to fix file permissions.

The general approach here is that, because we do not know the security
setup of the webserver, we apply our permission changes to all three
digits of the file permission (i.e. user, group and all).

To ensure that the values behave as expected (and numbers don't carry
from one digit to the next) we do the calculation on the octal value
using bitwise operations. This lets us remove, for example, 0222 from
0700 and get the correct value of 0500.

@param $file
 The name of the file with permissions to fix.
@param $mask
 The desired permissions for the file.
@param $message
 (optional) Whether to output messages. Defaults to TRUE.

@return
 TRUE/FALSE whether or not we were able to fix the file's permissions.
```

## Code

```php
function drupal_install_fix_file($file, $mask, $message = TRUE) {
  // If $file does not exist, fileperms() issues a PHP warning.
  if (!file_exists($file)) {
    return FALSE;
  }

  $mod = fileperms($file) & 0777;
  $masks = array(FILE_READABLE, FILE_WRITABLE, FILE_EXECUTABLE, FILE_NOT_READABLE, FILE_NOT_WRITABLE, FILE_NOT_EXECUTABLE);

  // FILE_READABLE, FILE_WRITABLE, and FILE_EXECUTABLE permission strings
  // can theoretically be 0400, 0200, and 0100 respectively, but to be safe
  // we set all three access types in case the administrator intends to
  // change the owner of settings.php after installation.
  foreach ($masks as $m) {
    if ($mask & $m) {
      switch ($m) {
        case FILE_READABLE:
          if (!is_readable($file)) {
            $mod |= 0444;
          }
          break;
        case FILE_WRITABLE:
          if (!is_writable($file)) {
            $mod |= 0222;
          }
          break;
        case FILE_EXECUTABLE:
          if (!is_executable($file)) {
            $mod |= 0111;
          }
          break;
        case FILE_NOT_READABLE:
          if (is_readable($file)) {
            $mod &= ~0444;
          }
          break;
        case FILE_NOT_WRITABLE:
          if (is_writable($file)) {
            $mod &= ~0222;
          }
          break;
        case FILE_NOT_EXECUTABLE:
          if (is_executable($file)) {
            $mod &= ~0111;
          }
          break;
      }
    }
  }

  // chmod() will work if the web server is running as owner of the file.
  // If PHP safe_mode is enabled the currently executing script must also
  // have the same owner.
  if (@chmod($file, $mod)) {
    return TRUE;
  }
  else {
    return FALSE;
  }
}
```

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
