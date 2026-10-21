# drupal_tempnam()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 2651–2668 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L2651-L2668)
- **Topics:** [file](../../topics/file.md), [php_wrappers](../../topics/php_wrappers.md)

## Signature

```php
function drupal_tempnam($directory, $prefix)
```

## Documentation

```text
Creates a file with a unique filename in the specified directory.

PHP's tempnam() does not return a URI like we want. This function
will return a URI if given a URI, or it will return a filepath if
given a filepath.

Compatibility: normal paths and stream wrappers.

@param $directory
  The directory where the temporary filename will be created.
@param $prefix
  The prefix of the generated temporary filename.
  Note: Windows uses only the first three characters of prefix.

@return
  The new temporary filename, or FALSE on failure.

@see tempnam()
@see http://drupal.org/node/515192
@ingroup php_wrappers
```

## Code

```php
function drupal_tempnam($directory, $prefix) {
  $scheme = file_uri_scheme($directory);

  if ($scheme && file_stream_wrapper_valid_scheme($scheme)) {
    $wrapper = file_stream_wrapper_get_instance_by_scheme($scheme);

    if ($filename = tempnam($wrapper->getDirectoryPath(), $prefix)) {
      return $scheme . '://' . drupal_basename($filename);
    }
    else {
      return FALSE;
    }
  }
  else {
    // Handle as a normal tempnam() call.
    return tempnam($directory, $prefix);
  }
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
