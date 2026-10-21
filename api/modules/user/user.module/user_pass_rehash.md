# user_pass_rehash()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 2453–2481 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L2453-L2481)
- **Module/theme:** user

## Signature

```php
function user_pass_rehash($password, $timestamp, $login, $uid, $mail = '')
```

## Documentation

```text
Creates a unique hash value for use in time-dependent per-user URLs.

This hash is normally used to build a unique and secure URL that is sent to
the user by email for purposes such as resetting the user's password. In
order to validate the URL, the same hash can be generated again, from the
same information, and compared to the hash value from the URL. The URL
normally contains both the time stamp and the numeric user ID. The login
timestamp and hashed password are retrieved from the database as necessary.
For a usage example, see user_cancel_url() and user_cancel_confirm().

@param string $password
  The hashed user account password value.
@param int $timestamp
  A UNIX timestamp, typically REQUEST_TIME.
@param int $login
  The UNIX timestamp of the user's last login.
@param int $uid
  The user ID of the user account.
@param string $mail
  The e-mail address of the user.

@return
  A string that is safe for use in URLs and SQL statements.
```

## Code

```php
function user_pass_rehash($password, $timestamp, $login, $uid, $mail = '') {
  // Backwards compatibility: Try to determine a $uid if one was not passed.
  // (Since $uid is a required parameter to this function, a PHP warning will
  // be generated if it's not provided, which is an indication that the calling
  // code should be updated. But the code below will try to generate a correct
  // hash in the meantime.)
  if (!isset($uid)) {
    $uids = db_query_range('SELECT uid FROM {users} WHERE pass = :password AND login = :login AND uid > 0', 0, 2, array(':password' => $password, ':login' => $login))->fetchCol();
    // If exactly one user account matches the provided password and login
    // timestamp, proceed with that $uid.
    if (count($uids) == 1) {
      $uid = reset($uids);
    }
    // Otherwise there is no safe hash to return, so return a random string
    // that will never be treated as a valid token.
    else {
      return drupal_random_key();
    }
  }

  // Backwards compatibility: If the $mail parameter is not provided, load it
  // from the user object.
  if (empty($mail)) {
    $account = user_load($uid);
    $mail = $account->mail;
  }

  return drupal_hmac_base64($timestamp . ':' . $login . ':' . $uid . ':' . $mail, drupal_get_hash_salt() . $password);
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
