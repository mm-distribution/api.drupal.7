# drupal_chmod()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 2341–2367 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L2341-L2367)
- **Topics:** [file](../../topics/file.md), [php_wrappers](../../topics/php_wrappers.md)

## Signature

```php
function drupal_chmod($uri, $mode = NULL)
```

## Documentation

```text
Sets the permissions on a file or directory.

This function will use the 'file_chmod_directory' and 'file_chmod_file'
variables for the default modes for directories and uploaded/generated
files. By default these will give everyone read access so that users
accessing the files with a user account without the webserver group (e.g.
via FTP) can read these files, and give group write permissions so webserver
group members (e.g. a vhost account) can alter files uploaded and owned by
the webserver.

PHP's chmod does not support stream wrappers so we use our wrapper
implementation which interfaces with chmod() by default. Contrib wrappers
may override this behavior in their implementations as needed.

@param $uri
  A string containing a URI file, or directory path.
@param $mode
  Integer value for the permissions. Consult PHP chmod() documentation for
  more information.

@return
  TRUE for success, FALSE in the event of an error.

@ingroup php_wrappers
```

## Code

```php
function drupal_chmod($uri, $mode = NULL) {
  if (!isset($mode)) {
    if (is_dir($uri)) {
      $mode = variable_get('file_chmod_directory', 0775);
    }
    else {
      $mode = variable_get('file_chmod_file', 0664);
    }
  }

  // If this URI is a stream, pass it off to the appropriate stream wrapper.
  // Otherwise, attempt PHP's chmod. This allows use of drupal_chmod even
  // for unmanaged files outside of the stream wrapper interface.
  if ($wrapper = file_stream_wrapper_get_instance_by_uri($uri)) {
    if ($wrapper->chmod($mode)) {
      return TRUE;
    }
  }
  else {
    if (@chmod($uri, $mode)) {
      return TRUE;
    }
  }

  watchdog('file', 'The file permissions could not be set on %uri.', array('%uri' => $uri), WATCHDOG_ERROR);
  return FALSE;
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
