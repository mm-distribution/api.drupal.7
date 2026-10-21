# user_hash_password()

- **Type:** Function
- **File:** [`includes/password.inc`](_file.md), lines 211–217 · [local source](../../../source/includes/password.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/password.inc#L211-L217)

## Signature

```php
function user_hash_password($password, $count_log2 = 0)
```

## Documentation

```text
Hash a password using a secure hash.

@param $password
  A plain-text password.
@param $count_log2
  Optional integer to specify the iteration count. Generally used only during
  mass operations where a value less than the default is needed for speed.

@return
  A string containing the hashed password (and a salt), or FALSE on failure.
```

## Code

```php
function user_hash_password($password, $count_log2 = 0) {
  if (empty($count_log2)) {
    // Use the standard iteration count.
    $count_log2 = variable_get('password_count_log2', DRUPAL_HASH_COUNT);
  }
  return _password_crypt('sha512', $password, _password_generate_salt($count_log2));
}
```

---
_Drupal 7.103 · [includes/password.inc](https://github.com/drupal/drupal/blob/7.103/includes/password.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
