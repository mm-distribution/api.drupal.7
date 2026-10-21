# file_directory_temp()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 2673–2721 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L2673-L2721)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_directory_temp()
```

## Documentation

```text
Gets the path of system-appropriate temporary directory.
```

## Code

```php
function file_directory_temp() {
  $temporary_directory = variable_get('file_temporary_path', NULL);

  if (empty($temporary_directory)) {
    $directories = array();

    // Has PHP been set with an upload_tmp_dir?
    if (ini_get('upload_tmp_dir')) {
      $directories[] = ini_get('upload_tmp_dir');
    }

    // Operating system specific dirs.
    if (substr(PHP_OS, 0, 3) == 'WIN') {
      $directories[] = 'c:\\windows\\temp';
      $directories[] = 'c:\\winnt\\temp';
    }
    else {
      $directories[] = '/tmp';
    }
    // PHP may be able to find an alternative tmp directory.
    // This function exists in PHP 5 >= 5.2.1, but Drupal
    // requires PHP 5 >= 5.2.0, so we check for it.
    if (function_exists('sys_get_temp_dir')) {
      $directories[] = sys_get_temp_dir();
    }

    foreach ($directories as $directory) {
      if (is_dir($directory) && is_writable($directory)) {
        $temporary_directory = $directory;
        break;
      }
    }

    if (empty($temporary_directory)) {
      // If no directory has been found default to 'files/tmp'.
      $temporary_directory = variable_get('file_public_path', conf_path() . '/files') . '/tmp';

      // Windows accepts paths with either slash (/) or backslash (\), but will
      // not accept a path which contains both a slash and a backslash. Since
      // the 'file_public_path' variable may have either format, we sanitize
      // everything to use slash which is supported on all platforms.
      $temporary_directory = str_replace('\\', '/', $temporary_directory);
    }
    // Save the path of the discovered directory.
    variable_set('file_temporary_path', $temporary_directory);
  }

  return $temporary_directory;
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
