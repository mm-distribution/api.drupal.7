# file_create_htaccess()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 486–510 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L486-L510)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_create_htaccess($directory, $private = TRUE, $force_overwrite = FALSE)
```

## Documentation

```text
Creates a .htaccess file in the given directory.

@param $directory
  The directory.
@param $private
  FALSE indicates that $directory should be an open and public directory.
  The default is TRUE which indicates a private and protected directory.
@param $force_overwrite
  Set to TRUE to attempt to overwrite the existing .htaccess file if one is
  already present. Defaults to FALSE.
```

## Code

```php
function file_create_htaccess($directory, $private = TRUE, $force_overwrite = FALSE) {
  if (file_uri_scheme($directory)) {
    $directory = file_stream_wrapper_uri_normalize($directory);
  }
  else {
    $directory = rtrim($directory, '/\\');
  }
  $htaccess_path =  $directory . '/.htaccess';

  if (file_exists($htaccess_path) && !$force_overwrite) {
    // Short circuit if the .htaccess file already exists.
    return;
  }

  $htaccess_lines = file_htaccess_lines($private);

  // Write the .htaccess file.
  if (file_put_contents($htaccess_path, $htaccess_lines)) {
    drupal_chmod($htaccess_path, 0444);
  }
  else {
    $variables = array('%directory' => $directory, '!htaccess' => '<br />' . nl2br(check_plain($htaccess_lines)));
    watchdog('security', "Security warning: Couldn't write .htaccess file. Please create a .htaccess file in your %directory directory which contains the following lines: <code>!htaccess</code>", $variables, WATCHDOG_ERROR);
  }
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
