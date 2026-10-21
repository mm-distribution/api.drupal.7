# user_set_authmaps()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 2091–2110 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L2091-L2110)
- **Module/theme:** user

## Signature

```php
function user_set_authmaps($account, $authmaps)
```

## Documentation

```text
Save mappings of which external authentication module(s) authenticated
a user. Maps external usernames to user ids in the users table.

@param $account
  A user object.
@param $authmaps
  An associative array with a compound key and the username as the value.
  The key is made up of 'authname_' plus the name of the external authentication
  module.
@see user_external_login_register()
```

## Code

```php
function user_set_authmaps($account, $authmaps) {
  foreach ($authmaps as $key => $value) {
    $module = explode('_', $key, 2);
    if ($value) {
      db_merge('authmap')
        ->key(array(
          'uid' => $account->uid,
          'module' => $module[1],
        ))
        ->fields(array('authname' => $value))
        ->execute();
    }
    else {
      db_delete('authmap')
        ->condition('uid', $account->uid)
        ->condition('module', $module[1])
        ->execute();
    }
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
