# drupal_add_http_header()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 1466–1485 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L1466-L1485)

## Signature

```php
function drupal_add_http_header($name, $value, $append = FALSE)
```

## Documentation

```text
Sets an HTTP response header for the current page.

Note: When sending a Content-Type header, always include a 'charset' type,
too. This is necessary to avoid security bugs (e.g. UTF-7 XSS).

@param $name
  The HTTP header name, or the special 'Status' header name.
@param $value
  The HTTP header value; if equal to FALSE, the specified header is unset.
  If $name is 'Status', this is expected to be a status code followed by a
  reason phrase, e.g. "404 Not Found".
@param $append
  Whether to append the value to an existing header or to replace it.
```

## Code

```php
function drupal_add_http_header($name, $value, $append = FALSE) {
  // The headers as name/value pairs.
  $headers = &drupal_static('drupal_http_headers', array());

  $name_lower = strtolower($name);
  _drupal_set_preferred_header_name($name);

  if ($value === FALSE) {
    $headers[$name_lower] = FALSE;
  }
  elseif (isset($headers[$name_lower]) && $append) {
    // Multiple headers with identical names may be combined using comma (RFC
    // 2616, section 4.2).
    $headers[$name_lower] .= ',' . $value;
  }
  else {
    $headers[$name_lower] = $value;
  }
  drupal_send_headers(array($name => $headers[$name_lower]), TRUE);
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
