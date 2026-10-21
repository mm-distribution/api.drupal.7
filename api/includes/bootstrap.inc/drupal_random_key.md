# drupal_random_key()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 2291–2293 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L2291-L2293)

## Signature

```php
function drupal_random_key($byte_count = 32)
```

## Documentation

```text
Returns a URL-safe, base64 encoded string of highly randomized bytes (over the full 8-bit range).

@param $byte_count
  The number of random bytes to fetch and base64 encode.

@return string
  A base-64 encoded string, with + replaced with -, / with _ and any =
  padding characters removed.
```

## Code

```php
function drupal_random_key($byte_count = 32) {
  return drupal_base64_encode(drupal_random_bytes($byte_count));
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
