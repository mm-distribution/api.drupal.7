# file_create_filename()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 1250–1293 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L1250-L1293)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_create_filename($basename, $directory)
```

## Documentation

```text
Creates a full file path from a directory and filename.

If a file with the specified name already exists, an alternative will be
used.

@param $basename
  String filename
@param $directory
  String containing the directory or parent URI.

@return
  File path consisting of $directory and a unique filename based off
  of $basename.

@throws RuntimeException
  Thrown if the $basename is not valid UTF-8 or another error occurs
  stripping control characters.
```

## Code

```php
function file_create_filename($basename, $directory) {
  $original = $basename;
  // Strip control characters (ASCII value < 32). Though these are allowed in
  // some filesystems, not many applications handle them well.
  $basename = preg_replace('/[\x00-\x1F]/u', '_', $basename);
  if (preg_last_error() !== PREG_NO_ERROR) {
    throw new RuntimeException(sprintf("Invalid filename '%s'", $original));
  }

  if (substr(PHP_OS, 0, 3) == 'WIN') {
    // These characters are not allowed in Windows filenames
    $basename = str_replace(array(':', '*', '?', '"', '<', '>', '|'), '_', $basename);
  }

  // A URI or path may already have a trailing slash or look like "public://".
  if (substr($directory, -1) == '/') {
    $separator = '';
  }
  else {
    $separator = '/';
  }

  $destination = $directory . $separator . $basename;

  if (file_exists($destination)) {
    // Destination file already exists, generate an alternative.
    $pos = strrpos($basename, '.');
    if ($pos !== FALSE) {
      $name = substr($basename, 0, $pos);
      $ext = substr($basename, $pos);
    }
    else {
      $name = $basename;
      $ext = '';
    }

    $counter = 0;
    do {
      $destination = $directory . $separator . $name . '_' . $counter++ . $ext;
    } while (file_exists($destination));
  }

  return $destination;
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
