# drupal_hash_base64()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 2428–2432 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L2428-L2432)

## Signature

```php
function drupal_hash_base64($data)
```

## Documentation

```text
Calculates a base-64 encoded, URL-safe sha-256 hash.

@param $data
  String to be hashed.

@return
  A base-64 encoded sha-256 hash, with + replaced with -, / with _ and
  any = padding characters removed.
```

## Code

```php
function drupal_hash_base64($data) {
  $hash = base64_encode(hash('sha256', $data, TRUE));
  // Modify the hash so it's safe to use in URLs.
  return strtr($hash, array('+' => '-', '/' => '_', '=' => ''));
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
