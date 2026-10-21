# _password_enforce_log2_boundaries()

- **Type:** Function
- **File:** [`includes/password.inc`](_file.md), lines 121–130 · [local source](../../../source/includes/password.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/password.inc#L121-L130)

## Signature

```php
function _password_enforce_log2_boundaries($count_log2)
```

## Documentation

```text
Ensures that $count_log2 is within set bounds.

@param $count_log2
  Integer that determines the number of iterations used in the hashing
  process. A larger value is more secure, but takes more time to complete.

@return
  Integer within set bounds that is closest to $count_log2.
```

## Code

```php
function _password_enforce_log2_boundaries($count_log2) {
  if ($count_log2 < DRUPAL_MIN_HASH_COUNT) {
    return DRUPAL_MIN_HASH_COUNT;
  }
  elseif ($count_log2 > DRUPAL_MAX_HASH_COUNT) {
    return DRUPAL_MAX_HASH_COUNT;
  }

  return (int) $count_log2;
}
```

---
_Drupal 7.103 · [includes/password.inc](https://github.com/drupal/drupal/blob/7.103/includes/password.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
