# file_get_mimetype()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 2304–2313 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L2304-L2313)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_get_mimetype($uri, $mapping = NULL)
```

## Documentation

```text
Determines an Internet Media Type or MIME type from a filename.

@param $uri
  A string containing the URI, path, or filename.
@param $mapping
  An optional map of extensions to their mimetypes, in the form:
   - 'mimetypes': a list of mimetypes, keyed by an identifier,
   - 'extensions': the mapping itself, an associative array in which
     the key is the extension (lowercase) and the value is the mimetype
     identifier. If $mapping is NULL file_mimetype_mapping() is called.

@return
  The internet media type registered for the extension or
  application/octet-stream for unknown extensions.

@see file_default_mimetype_mapping()
```

## Code

```php
function file_get_mimetype($uri, $mapping = NULL) {
  if ($wrapper = file_stream_wrapper_get_instance_by_uri($uri)) {
    return $wrapper->getMimeType($uri, $mapping);
  }
  else {
    // getMimeType() is not implementation specific, so we can directly
    // call it without an instance.
    return DrupalLocalStreamWrapper::getMimeType($uri, $mapping);
  }
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
