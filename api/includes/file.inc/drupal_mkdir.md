# drupal_mkdir()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 2522–2582 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L2522-L2582)
- **Topics:** [file](../../topics/file.md), [php_wrappers](../../topics/php_wrappers.md)

## Signature

```php
function drupal_mkdir($uri, $mode = NULL, $recursive = FALSE, $context = NULL)
```

## Documentation

```text
Creates a directory, optionally creating missing components in the path to
the directory.

When PHP's mkdir() creates a directory, the requested mode is affected by the
process's umask. This function overrides the umask and sets the mode
explicitly for all directory components created.

@param $uri
  A URI or pathname.
@param $mode
  Mode given to created directories. Defaults to the directory mode
  configured in the Drupal installation. It must have a leading zero.
@param $recursive
  Create directories recursively, defaults to FALSE. Cannot work with a mode
  which denies writing or execution to the owner of the process.
@param $context
  Refer to http://php.net/manual/ref.stream.php

@return
  Boolean TRUE on success, or FALSE on failure.

@see mkdir()
@see http://drupal.org/node/515192
@ingroup php_wrappers
```

## Code

```php
function drupal_mkdir($uri, $mode = NULL, $recursive = FALSE, $context = NULL) {
  if (!isset($mode)) {
    $mode = variable_get('file_chmod_directory', 0775);
  }

  // If the URI has a scheme, don't override the umask - schemes can handle this
  // issue in their own implementation.
  if (file_uri_scheme($uri)) {
    return _drupal_mkdir_call($uri, $mode, $recursive, $context);
  }

  // If recursive, create each missing component of the parent directory
  // individually and set the mode explicitly to override the umask.
  if ($recursive) {
    // Ensure the path is using DIRECTORY_SEPARATOR, and trim off any trailing
    // slashes because they can throw off the loop when creating the parent
    // directories.
    $uri = rtrim(str_replace('/', DIRECTORY_SEPARATOR, $uri), DIRECTORY_SEPARATOR);
    // Determine the components of the path.
    $components = explode(DIRECTORY_SEPARATOR, $uri);
    // If the filepath is absolute the first component will be empty as there
    // will be nothing before the first slash.
    if ($components[0] == '') {
      $recursive_path = DIRECTORY_SEPARATOR;
      // Get rid of the empty first component.
      array_shift($components);
    }
    else {
      $recursive_path = '';
    }
    // Don't handle the top-level directory in this loop.
    array_pop($components);
    // Create each component if necessary.
    foreach ($components as $component) {
      $recursive_path .= $component;

      if (!file_exists($recursive_path)) {
        $success = _drupal_mkdir_call($recursive_path, $mode, FALSE, $context);
        // If the operation failed, check again if the directory was created
        // by another process/server, only report a failure if not.
        if (!$success && !file_exists($recursive_path)) {
          return FALSE;
        }
        // Not necessary to use self::chmod() as there is no scheme.
        if (!chmod($recursive_path, $mode)) {
          return FALSE;
        }
      }

      $recursive_path .= DIRECTORY_SEPARATOR;
    }
  }

  // Do not check if the top-level directory already exists, as this condition
  // must cause this function to fail.
  if (!_drupal_mkdir_call($uri, $mode, FALSE, $context)) {
    return FALSE;
  }
  // Not necessary to use drupal_chmod() as there is no scheme.
  return chmod($uri, $mode);
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
