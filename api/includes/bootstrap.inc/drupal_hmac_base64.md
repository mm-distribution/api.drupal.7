# drupal_hmac_base64()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 2408–2416 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L2408-L2416)

## Signature

```php
function drupal_hmac_base64($data, $key)
```

## Documentation

```text
Calculates a base-64 encoded, URL-safe sha-256 hmac.

@param string $data
  String to be validated with the hmac.
@param string $key
  A secret string key.

@return string
  A base-64 encoded sha-256 hmac, with + replaced with -, / with _ and
  any = padding characters removed.
```

## Code

```php
function drupal_hmac_base64($data, $key) {
  // Casting $data and $key to strings here is necessary to avoid empty string
  // results of the hash function if they are not scalar values. As this
  // function is used in security-critical contexts like token validation it is
  // important that it never returns an empty string.
  $hmac = base64_encode(hash_hmac('sha256', (string) $data, (string) $key, TRUE));
  // Modify the hmac so it's safe to use in URLs.
  return strtr($hmac, array('+' => '-', '/' => '_', '=' => ''));
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
