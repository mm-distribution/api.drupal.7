# drupal_is_https()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 752–754 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L752-L754)

## Signature

```php
function drupal_is_https()
```

## Documentation

```text
Checks whether an HTTPS request is being served.

@return bool
  TRUE if the request is HTTPS, FALSE otherwise.
```

## Code

```php
function drupal_is_https() {
  return isset($_SERVER['HTTPS']) && strtolower($_SERVER['HTTPS']) == 'on';
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
