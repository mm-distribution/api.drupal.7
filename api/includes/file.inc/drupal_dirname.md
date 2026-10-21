# drupal_dirname()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 2456–2465 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L2456-L2465)
- **Topics:** [file](../../topics/file.md), [php_wrappers](../../topics/php_wrappers.md)

## Signature

```php
function drupal_dirname($uri)
```

## Documentation

```text
Gets the name of the directory from a given path.

PHP's dirname() does not properly pass streams, so this function fills
that gap. It is backwards compatible with normal paths and will use
PHP's dirname() as a fallback.

Compatibility: normal paths and stream wrappers.

@param $uri
  A URI or path.

@return
  A string containing the directory name.

@see dirname()
@see http://drupal.org/node/515192
@ingroup php_wrappers
```

## Code

```php
function drupal_dirname($uri) {
  $scheme = file_uri_scheme($uri);

  if ($scheme && file_stream_wrapper_valid_scheme($scheme)) {
    return file_stream_wrapper_get_instance_by_scheme($scheme)->dirname($uri);
  }
  else {
    return dirname($uri);
  }
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
