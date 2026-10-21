# drupal_get_hash_salt()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 2652–2657 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L2652-L2657)

## Signature

```php
function drupal_get_hash_salt()
```

## Documentation

```text
Gets a salt useful for hardening against SQL injection.

@return
  A salt based on information in settings.php, not in the database.
```

## Code

```php
function drupal_get_hash_salt() {
  global $drupal_hash_salt, $databases;
  // If the $drupal_hash_salt variable is empty, a hash of the serialized
  // database credentials is used as a fallback salt.
  return empty($drupal_hash_salt) ? hash('sha256', serialize($databases)) : $drupal_hash_salt;
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
