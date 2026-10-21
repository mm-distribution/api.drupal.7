# authorize_get_filetransfer()

- **Type:** Function
- **File:** [`includes/authorize.inc`](_file.md), lines 314–329 · [local source](../../../source/includes/authorize.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/authorize.inc#L314-L329)

## Signature

```php
function authorize_get_filetransfer($backend, $settings = array())
```

## Documentation

```text
Gets a FileTransfer class for a specific transfer method and settings.

@param $backend
  The FileTransfer backend to get the class for.
@param $settings
  Array of settings for the FileTransfer.

@return
  An instantiated FileTransfer object for the requested method and settings,
  or FALSE if there was an error finding or instantiating it.
```

## Code

```php
function authorize_get_filetransfer($backend, $settings = array()) {
  $filetransfer = FALSE;
  if (!empty($_SESSION['authorize_filetransfer_info'][$backend])) {
    $backend_info = $_SESSION['authorize_filetransfer_info'][$backend];
    if (!empty($backend_info['file'])) {
      $file = $backend_info['file path'] . '/' . $backend_info['file'];
      require_once $file;
    }
    if (class_exists($backend_info['class'])) {
      // PHP 5.2 doesn't support $class::factory() syntax, so we have to
      // use call_user_func_array() until we can require PHP 5.3.
      $filetransfer = call_user_func_array(array($backend_info['class'], 'factory'), array(DRUPAL_ROOT, $settings));
    }
  }
  return $filetransfer;
}
```

---
_Drupal 7.103 · [includes/authorize.inc](https://github.com/drupal/drupal/blob/7.103/includes/authorize.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
