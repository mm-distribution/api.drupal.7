# drupal_valid_http_host()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 735–744 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L735-L744)

## Signature

```php
function drupal_valid_http_host($host)
```

## Documentation

```text
Validates that a hostname (for example $_SERVER['HTTP_HOST']) is safe.

@return bool
  TRUE if it only contains valid characters, FALSE otherwise.
```

## Code

```php
function drupal_valid_http_host($host) {
  // Limit the length of the host name to 1000 bytes to prevent DoS attacks with
  // long host names.
  return strlen($host) <= 1000
    // Limit the number of subdomains and port separators to prevent DoS attacks
    // in conf_path().
    && substr_count($host, '.') <= 100
    && substr_count($host, ':') <= 100
    && preg_match('/^\[?(?:[a-zA-Z0-9-:\]_]+\.?)+$/', $host);
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
