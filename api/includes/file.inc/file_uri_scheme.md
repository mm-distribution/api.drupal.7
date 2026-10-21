# file_uri_scheme()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 206–209 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L206-L209)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_uri_scheme($uri)
```

## Documentation

```text
Returns the scheme of a URI (e.g. a stream).

@param $uri
  A stream, referenced as "scheme://target".

@return
  A string containing the name of the scheme, or FALSE if none. For example,
  the URI "public://example.txt" would return "public".

@see file_uri_target()
```

## Code

```php
function file_uri_scheme($uri) {
  $position = strpos((string) $uri, '://');
  return $position ? substr($uri, 0, $position) : FALSE;
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
