# file_destination()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 1014–1036 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L1014-L1036)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_destination($destination, $replace)
```

## Documentation

```text
Determines the destination path for a file.

@param $destination
  A string specifying the desired final URI or filepath.
@param $replace
  Replace behavior when the destination file already exists.
  - FILE_EXISTS_REPLACE - Replace the existing file.
  - FILE_EXISTS_RENAME - Append _{incrementing number} until the filename is
      unique.
  - FILE_EXISTS_ERROR - Do nothing and return FALSE.

@return
  The destination filepath, or FALSE if the file already exists
  and FILE_EXISTS_ERROR is specified.

@throws RuntimeException
  Thrown if the filename contains invalid UTF-8.
```

## Code

```php
function file_destination($destination, $replace) {
  $basename = drupal_basename($destination);
  if (!drupal_validate_utf8($basename)) {
    throw new RuntimeException(sprintf("Invalid filename '%s'", $basename));
  }
  if (file_exists($destination)) {
    switch ($replace) {
      case FILE_EXISTS_REPLACE:
        // Do nothing here, we want to overwrite the existing file.
        break;

      case FILE_EXISTS_RENAME:
        $directory = drupal_dirname($destination);
        $destination = file_create_filename($basename, $directory);
        break;

      case FILE_EXISTS_ERROR:
        // Error reporting handled by calling function.
        return FALSE;
    }
  }
  return $destination;
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
