# user_needs_new_hash()

- **Type:** Function
- **File:** [`includes/password.inc`](_file.md), lines 282–291 · [local source](../../../source/includes/password.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/password.inc#L282-L291)

## Signature

```php
function user_needs_new_hash($account)
```

## Documentation

```text
Check whether a user's hashed password needs to be replaced with a new hash.

This is typically called during the login process when the plain text
password is available. A new hash is needed when the desired iteration count
has changed through a change in the variable password_count_log2 or
DRUPAL_HASH_COUNT or if the user's password hash was generated in an update
like user_update_7000().

Alternative implementations of this function might use other criteria based
on the fields in $account.

@param $account
  A user object with at least the fields from the {users} table.

@return
  TRUE or FALSE.
```

## Code

```php
function user_needs_new_hash($account) {
  // Check whether this was an updated password.
  if ((substr($account->pass, 0, 3) != '$S$') || (strlen($account->pass) != DRUPAL_HASH_LENGTH)) {
    return TRUE;
  }
  // Ensure that $count_log2 is within set bounds.
  $count_log2 = _password_enforce_log2_boundaries(variable_get('password_count_log2', DRUPAL_HASH_COUNT));
  // Check whether the iteration count used differs from the standard number.
  return (_password_get_count_log2($account->pass) !== $count_log2);
}
```

---
_Drupal 7.103 · [includes/password.inc](https://github.com/drupal/drupal/blob/7.103/includes/password.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
