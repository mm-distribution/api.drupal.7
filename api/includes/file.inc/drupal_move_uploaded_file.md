# drupal_move_uploaded_file()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 1707–1722 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L1707-L1722)
- **Topics:** [file](../../topics/file.md), [php_wrappers](../../topics/php_wrappers.md)

## Signature

```php
function drupal_move_uploaded_file($filename, $uri)
```

## Documentation

```text
Moves an uploaded file to a new location.

PHP's move_uploaded_file() does not properly support streams if safe_mode
or open_basedir are enabled, so this function fills that gap.

Compatibility: normal paths and stream wrappers.

@param $filename
  The filename of the uploaded file.
@param $uri
  A string containing the destination URI of the file.

@return
  TRUE on success, or FALSE on failure.

@see move_uploaded_file()
@see http://drupal.org/node/515192
@ingroup php_wrappers
```

## Code

```php
function drupal_move_uploaded_file($filename, $uri) {
  $result = @move_uploaded_file($filename, $uri);
  // PHP's move_uploaded_file() does not properly support streams if safe_mode
  // or open_basedir are enabled so if the move failed, try finding a real path
  // and retry the move operation.
  if (!$result) {
    if ($realpath = drupal_realpath($uri)) {
      $result = move_uploaded_file($filename, $realpath);
    }
    else {
      $result = move_uploaded_file($filename, $uri);
    }
  }

  return $result;
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
