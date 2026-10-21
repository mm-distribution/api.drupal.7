# user_external_login_register()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 2363–2386 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L2363-L2386)
- **Module/theme:** user

## Signature

```php
function user_external_login_register($name, $module)
```

## Documentation

```text
Helper function for authentication modules. Either logs in or registers
the current user, based on username. Either way, the global $user object is
populated and login tasks are performed.
```

## Code

```php
function user_external_login_register($name, $module) {
  $account = user_external_load($name);
  if (!$account) {
    // Register this new user.
    $userinfo = array(
      'name' => $name,
      'pass' => user_password(),
      'init' => $name,
      'status' => 1,
      'access' => REQUEST_TIME
    );
    $account = user_save(drupal_anonymous_user(), $userinfo);
    // Terminate if an error occurred during user_save().
    if (!$account) {
      drupal_set_message(t("Error saving user account."), 'error');
      return;
    }
    user_set_authmaps($account, array("authname_$module" => $name));
  }

  // Log user in.
  $form_state['uid'] = $account->uid;
  user_login_submit(array(), $form_state);
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
