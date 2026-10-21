# _drupal_should_strip_sensitive_headers_on_http_redirect()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 1146–1161 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L1146-L1161)
- **Topics:** [http_handling](../../topics/http_handling.md)

## Signature

```php
function _drupal_should_strip_sensitive_headers_on_http_redirect($url, $location)
```

## Documentation

```text
Determine whether to strip sensitive headers from a request when redirected.

@param string $url
  The url from the original outbound http request.

@param string $location
  The location to which the request has been redirected.

@return boolean
  Whether sensitive headers should be stripped from the request before
  following the redirect.
```

## Code

```php
function _drupal_should_strip_sensitive_headers_on_http_redirect($url, $location) {
  $url_parsed = parse_url($url);
  $location_parsed = parse_url($location);
  if (!isset($location_parsed['host'])) {
    return FALSE;
  }
  $strip_on_host_change = variable_get('drupal_http_request_strip_sensitive_headers_on_host_change', TRUE);
  $strip_on_https_downgrade = variable_get('drupal_http_request_strip_sensitive_headers_on_https_downgrade', TRUE);
  if ($strip_on_host_change && strcasecmp($url_parsed['host'], $location_parsed['host']) !== 0) {
    return TRUE;
  }
  if ($strip_on_https_downgrade && $url_parsed['scheme'] !== $location_parsed['scheme'] && 'https' !== $location_parsed['scheme']) {
    return TRUE;
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
