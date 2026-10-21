# user_authenticate()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 2293–2312 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L2293-L2312)
- **Module/theme:** user

## Signature

```php
function user_authenticate($name, $password)
```

## Documentation

```text
Try to validate the user's login credentials locally.

@param $name
  User name to authenticate.
@param $password
  A plain-text password, such as trimmed text from form values.
@return
  The user's uid on success, or FALSE on failure to authenticate.
```

## Code

```php
function user_authenticate($name, $password) {
  $uid = FALSE;
  if (!empty($name) && strlen(trim($password)) > 0) {
    $account = user_load_by_name($name);
    if ($account) {
      // Allow alternate password hashing schemes.
      require_once DRUPAL_ROOT . '/' . variable_get('password_inc', 'includes/password.inc');
      if (user_check_password($password, $account)) {
        // Successful authentication.
        $uid = $account->uid;

        // Update user to new password scheme if needed.
        if (user_needs_new_hash($account)) {
          user_save($account, array('pass' => $password));
        }
      }
    }
  }
  return $uid;
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
