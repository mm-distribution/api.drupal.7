# _drupal_get_cookie_domain()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 853–860 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L853-L860)

## Signature

```php
function _drupal_get_cookie_domain($host)
```

## Documentation

```text
Derive the cookie domain to use for session cookies.

@param $host
  The value of the HTTP host name.

@return
  The string to use as a cookie domain.
```

## Code

```php
function _drupal_get_cookie_domain($host) {
  $cookie_domain = $host;
  // Strip leading periods and port numbers from cookie domain.
  $cookie_domain = ltrim($cookie_domain, '.');
  $cookie_domain = explode(':', $cookie_domain);
  $cookie_domain = '.' . $cookie_domain[0];
  return $cookie_domain;
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
