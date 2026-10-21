# DrupalStreamWrapperInterface::getMimeType()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 173–173 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L173)
- **Class:** [DrupalStreamWrapperInterface](../DrupalStreamWrapperInterface.md)

## Signature

```php
public static function getMimeType($uri, $mapping = NULL);
```

## Documentation

```text
Returns the MIME type of the resource.

@param $uri
  The URI, path, or filename.
@param $mapping
  An optional map of extensions to their mimetypes, in the form:
   - 'mimetypes': a list of mimetypes, keyed by an identifier,
   - 'extensions': the mapping itself, an associative array in which
     the key is the extension and the value is the mimetype identifier.

@return
  Returns a string containing the MIME type of the resource.
```

## Code

```php
  public static function getMimeType($uri, $mapping = NULL);
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
