# drupal_rmdir()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 2616–2627 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L2616-L2627)
- **Topics:** [file](../../topics/file.md), [php_wrappers](../../topics/php_wrappers.md)

## Signature

```php
function drupal_rmdir($uri, $context = NULL)
```

## Documentation

```text
Removes a directory.

PHP's rmdir() is broken on Windows, as it can fail to remove a directory
when it has a read-only flag set.

@param $uri
  A URI or pathname.
@param $context
  Refer to http://php.net/manual/ref.stream.php

@return
  Boolean TRUE on success, or FALSE on failure.

@see rmdir()
@ingroup php_wrappers
```

## Code

```php
function drupal_rmdir($uri, $context = NULL) {
  $scheme = file_uri_scheme($uri);
  if ((!$scheme || !file_stream_wrapper_valid_scheme($scheme)) && (substr(PHP_OS, 0, 3) == 'WIN')) {
    chmod($uri, 0700);
  }
  if ($context) {
    return rmdir($uri, $context);
  }
  else {
    return rmdir($uri);
  }
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
