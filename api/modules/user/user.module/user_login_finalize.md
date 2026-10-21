# user_login_finalize()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 2325–2343 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L2325-L2343)
- **Module/theme:** user

## Signature

```php
function user_login_finalize(&$form_state = array())
```

## Documentation

```text
Finalize the login process. Must be called when logging in a user.

The function records a watchdog message about the new session, saves the
login timestamp, calls hook_user_login(), and generates a new session.

@param array $form_state
  A keyed array containing the current state of the login form.

@see hook_user_login()
```

## Code

```php
function user_login_finalize(&$form_state = array()) {
  global $user;
  watchdog('user', 'Session opened for %name.', array('%name' => $user->name));
  // Update the user table timestamp noting user has logged in.
  // This is also used to invalidate one-time login links.
  $user->login = REQUEST_TIME;
  db_update('users')
    ->fields(array('login' => $user->login))
    ->condition('uid', $user->uid)
    ->execute();

  // Regenerate the session ID to prevent against session fixation attacks.
  // This is called before hook_user_login() in case one of those functions
  // fails or incorrectly does a redirect which would leave the old session in
  // place.
  drupal_session_regenerate();

  user_module_invoke('login', $form_state, $user);
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
