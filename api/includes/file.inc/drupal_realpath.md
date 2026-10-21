# drupal_realpath()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 2420–2435 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L2420-L2435)
- **Topics:** [file](../../topics/file.md), [php_wrappers](../../topics/php_wrappers.md)

## Signature

```php
function drupal_realpath($uri)
```

## Documentation

```text
Resolves the absolute filepath of a local URI or filepath.

The use of drupal_realpath() is discouraged, because it does not work for
remote URIs. Except in rare cases, URIs should not be manually resolved.

Only use this function if you know that the stream wrapper in the URI uses
the local file system, and you need to pass an absolute path to a function
that is incompatible with stream URIs.

@param string $uri
  A stream wrapper URI or a filepath, possibly including one or more symbolic
  links.

@return string|false
  The absolute local filepath (with no symbolic links), or FALSE on failure.

@see DrupalStreamWrapperInterface::realpath()
@see http://php.net/manual/function.realpath.php
@ingroup php_wrappers
```

## Code

```php
function drupal_realpath($uri) {
  // If this URI is a stream, pass it off to the appropriate stream wrapper.
  // Otherwise, attempt PHP's realpath. This allows use of drupal_realpath even
  // for unmanaged files outside of the stream wrapper interface.
  if ($wrapper = file_stream_wrapper_get_instance_by_uri($uri)) {
    return $wrapper->realpath();
  }
  // Check that the URI has a value. There is a bug in PHP 5.2 on *BSD systems
  // that makes realpath not return FALSE as expected when passing an empty
  // variable.
  // @todo Remove when Drupal drops support for PHP 5.2.
  elseif (!empty($uri)) {
    return realpath($uri);
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
