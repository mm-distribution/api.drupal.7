# user_check_password()

- **Type:** Function
- **File:** [`includes/password.inc`](_file.md), lines 234–262 · [local source](../../../source/includes/password.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/password.inc#L234-L262)

## Signature

```php
function user_check_password($password, $account)
```

## Documentation

```text
Check whether a plain text password matches a stored hashed password.

Alternative implementations of this function may use other data in the
$account object, for example the uid to look up the hash in a custom table
or remote database.

@param $password
  A plain-text password
@param $account
  A user object with at least the fields from the {users} table.

@return
  TRUE or FALSE.
```

## Code

```php
function user_check_password($password, $account) {
  if (substr($account->pass, 0, 2) == 'U$') {
    // This may be an updated password from user_update_7000(). Such hashes
    // have 'U' added as the first character and need an extra md5().
    $stored_hash = substr($account->pass, 1);
    $password = md5($password);
  }
  else {
    $stored_hash = $account->pass;
  }

  $type = substr($stored_hash, 0, 3);
  switch ($type) {
    case '$S$':
      // A normal Drupal 7 password using sha512.
      $hash = _password_crypt('sha512', $password, $stored_hash);
      break;
    case '$H$':
      // phpBB3 uses "$H$" for the same thing as "$P$".
    case '$P$':
      // A phpass password generated using md5.  This is an
      // imported password or from an earlier Drupal version.
      $hash = _password_crypt('md5', $password, $stored_hash);
      break;
    default:
      return FALSE;
  }
  return ($hash && $stored_hash == $hash);
}
```

---
_Drupal 7.103 · [includes/password.inc](https://github.com/drupal/drupal/blob/7.103/includes/password.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
