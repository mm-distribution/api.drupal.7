# drupal_check_trusted_hosts()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 3974–3991 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L3974-L3991)

## Signature

```php
function drupal_check_trusted_hosts($host, array $host_patterns)
```

## Documentation

```text
Checks trusted HTTP Host headers to protect against header injection attacks.

@param string|null $host
  The host name.
@param array $host_patterns
  The array of trusted host patterns.

@return bool
  TRUE if the host is trusted, FALSE otherwise.
```

## Code

```php
function drupal_check_trusted_hosts($host, array $host_patterns) {
  if (!empty($host) && !empty($host_patterns)) {
    // Trim and remove the port number from host; host is lowercase as per
    // RFC 952/2181.
    $host = strtolower(preg_replace('/:\d+$/', '', trim($host)));

    foreach ($host_patterns as $pattern) {
      $pattern = sprintf('{%s}i', $pattern);
      if (preg_match($pattern, $host)) {
        return TRUE;
      }
    }

    return FALSE;
  }

  return TRUE;
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
