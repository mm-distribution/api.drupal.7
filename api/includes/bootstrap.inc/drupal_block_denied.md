# drupal_block_denied()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 2272–2279 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L2272-L2279)

## Signature

```php
function drupal_block_denied($ip)
```

## Documentation

```text
Handles denied users.

@param $ip
  IP address to check. Prints a message and exits if access is denied.
```

## Code

```php
function drupal_block_denied($ip) {
  // Deny access to blocked IP addresses - t() is not yet available.
  if (drupal_is_denied($ip)) {
    header($_SERVER['SERVER_PROTOCOL'] . ' 403 Forbidden');
    print 'Sorry, ' . check_plain(ip_address()) . ' has been banned.';
    exit();
  }
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
