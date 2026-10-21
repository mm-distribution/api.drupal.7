# user_multiple_role_edit()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 3349–3382 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L3349-L3382)
- **Module/theme:** user

## Signature

```php
function user_multiple_role_edit($accounts, $operation, $rid)
```

## Documentation

```text
Callback function for admin mass adding/deleting a user role.
```

## Code

```php
function user_multiple_role_edit($accounts, $operation, $rid) {
  // The role name is not necessary as user_save() will reload the user
  // object, but some modules' hook_user() may look at this first.
  $role_name = db_query('SELECT name FROM {role} WHERE rid = :rid', array(':rid' => $rid))->fetchField();

  switch ($operation) {
    case 'add_role':
      $accounts = user_load_multiple($accounts);
      foreach ($accounts as $account) {
        // Skip adding the role to the user if they already have it.
        if ($account !== FALSE && !isset($account->roles[$rid])) {
          $roles = $account->roles + array($rid => $role_name);
          // For efficiency manually save the original account before applying
          // any changes.
          $account->original = clone $account;
          user_save($account, array('roles' => $roles));
        }
      }
      break;
    case 'remove_role':
      $accounts = user_load_multiple($accounts);
      foreach ($accounts as $account) {
        // Skip removing the role from the user if they already don't have it.
        if ($account !== FALSE && isset($account->roles[$rid])) {
          $roles = array_diff($account->roles, array($rid => $role_name));
          // For efficiency manually save the original account before applying
          // any changes.
          $account->original = clone $account;
          user_save($account, array('roles' => $roles));
        }
      }
      break;
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
