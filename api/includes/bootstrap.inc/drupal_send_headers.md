# drupal_send_headers()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 1536–1561 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L1536-L1561)

## Signature

```php
function drupal_send_headers($default_headers = array(), $only_default = FALSE)
```

## Documentation

```text
Sends the HTTP response headers that were previously set, adding defaults.

Headers are set in drupal_add_http_header(). Default headers are not set
if they have been replaced or unset using drupal_add_http_header().

@param array $default_headers
  (optional) An array of headers as name/value pairs.
@param bool $only_default
  (optional) If TRUE and headers have already been sent, send only the
  specified headers.
```

## Code

```php
function drupal_send_headers($default_headers = array(), $only_default = FALSE) {
  $headers_sent = &drupal_static(__FUNCTION__, FALSE);
  $headers = drupal_get_http_header();
  if ($only_default && $headers_sent) {
    $headers = array();
  }
  $headers_sent = TRUE;

  $header_names = _drupal_set_preferred_header_name();
  foreach ($default_headers as $name => $value) {
    $name_lower = strtolower($name);
    if (!isset($headers[$name_lower])) {
      $headers[$name_lower] = $value;
      $header_names[$name_lower] = $name;
    }
  }
  foreach ($headers as $name_lower => $value) {
    if ($name_lower == 'status') {
      header($_SERVER['SERVER_PROTOCOL'] . ' ' . $value);
    }
    // Skip headers that have been unset.
    elseif ($value !== FALSE) {
      header($header_names[$name_lower] . ': ' . $value);
    }
  }
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
