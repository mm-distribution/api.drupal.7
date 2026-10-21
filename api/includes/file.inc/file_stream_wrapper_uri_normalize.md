# file_stream_wrapper_uri_normalize()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 282–295 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L282-L295)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_stream_wrapper_uri_normalize($uri)
```

## Documentation

```text
Normalizes a URI by making it syntactically correct.

A stream is referenced as "scheme://target".

The following actions are taken:
- Remove trailing slashes from target
- Trim erroneous leading slashes from target. e.g. ":///" becomes "://".

@param $uri
  String reference containing the URI to normalize.

@return
  The normalized URI.
```

## Code

```php
function file_stream_wrapper_uri_normalize($uri) {
  // Inline file_uri_scheme() function call for performance reasons.
  $position = strpos($uri, '://');
  $scheme = $position ? substr($uri, 0, $position) : FALSE;

  if ($scheme && file_stream_wrapper_valid_scheme($scheme)) {
    $target = file_uri_target($uri);

    if ($target !== FALSE) {
      $uri = $scheme . '://' . $target;
    }
  }
  return $uri;
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
