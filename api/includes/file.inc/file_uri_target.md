# file_uri_target()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 250–255 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L250-L255)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_uri_target($uri)
```

## Documentation

```text
Returns the part of a URI after the schema.

@param $uri
  A stream, referenced as "scheme://target".

@return
  A string containing the target (path), or FALSE if none.
  For example, the URI "public://sample/test.txt" would return
  "sample/test.txt".

@see file_uri_scheme()
```

## Code

```php
function file_uri_target($uri) {
  $data = explode('://', $uri, 2);

  // Remove erroneous leading or trailing, forward-slashes and backslashes.
  return count($data) == 2 ? trim($data[1], '\/') : FALSE;
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
