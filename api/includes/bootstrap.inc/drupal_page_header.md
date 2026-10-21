# drupal_page_header()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 1577–1593 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L1577-L1593)

## Signature

```php
function drupal_page_header()
```

## Documentation

```text
Sets HTTP headers in preparation for a page response.

Authenticated users are always given a 'no-cache' header, and will fetch a
fresh page on every request. This prevents authenticated users from seeing
locally cached pages.

ETag and Last-Modified headers are not set per default for authenticated
users so that browsers do not send If-Modified-Since headers from
authenticated user pages. drupal_serve_page_from_cache() will set appropriate
ETag and Last-Modified headers for cached pages.

@see drupal_page_set_cache()
```

## Code

```php
function drupal_page_header() {
  $headers_sent = &drupal_static(__FUNCTION__, FALSE);
  if ($headers_sent) {
    return TRUE;
  }
  $headers_sent = TRUE;

  $default_headers = array(
    'Expires' => 'Sun, 19 Nov 1978 05:00:00 GMT',
    'Cache-Control' => 'no-cache, must-revalidate',
    // Prevent browsers from sniffing a response and picking a MIME type
    // different from the declared content-type, since that can lead to
    // XSS and other vulnerabilities.
    'X-Content-Type-Options' => 'nosniff',
  );
  drupal_send_headers($default_headers);
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
