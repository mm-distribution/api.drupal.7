# Updater::findInfoFile()

- **Type:** Method
- **File:** [`includes/updater.inc`](../_file.md), lines 148–162 · [local source](../../../../source/includes/updater.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc#L148-L162)
- **Class:** [Updater](../Updater.md)

## Signature

```php
public static function findInfoFile($directory)
```

## Documentation

```text
Figure out what the most important (or only) info file is in a directory.

Since there is no enforcement of which info file is the project's "main"
info file, this will get one with the same name as the directory, or the
first one it finds.  Not ideal, but needs a larger solution.

@param string $directory
  Directory to search in.

@return string
  Path to the info file.
```

## Code

```php
  public static function findInfoFile($directory) {
    $info_files = file_scan_directory($directory, '/.*\.info$/');
    if (!$info_files) {
      return FALSE;
    }
    foreach ($info_files as $info_file) {
      if (drupal_substr($info_file->filename, 0, -5) == drupal_basename($directory)) {
        // Info file Has the same name as the directory, return it.
        return $info_file->uri;
      }
    }
    // Otherwise, return the first one.
    $info_file = array_shift($info_files);
    return $info_file->uri;
  }
```

---
_Drupal 7.103 · [includes/updater.inc](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
