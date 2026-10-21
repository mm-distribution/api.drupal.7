# drupal_get_http_header()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 1498–1507 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L1498-L1507)

## Signature

```php
function drupal_get_http_header($name = NULL)
```

## Documentation

```text
Gets the HTTP response headers for the current page.

@param $name
  An HTTP header name. If omitted, all headers are returned as name/value
  pairs. If an array value is FALSE, the header has been unset.

@return
  A string containing the header value, or FALSE if the header has been set,
  or NULL if the header has not been set.
```

## Code

```php
function drupal_get_http_header($name = NULL) {
  $headers = &drupal_static('drupal_http_headers', array());
  if (isset($name)) {
    $name = strtolower($name);
    return isset($headers[$name]) ? $headers[$name] : NULL;
  }
  else {
    return $headers;
  }
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
