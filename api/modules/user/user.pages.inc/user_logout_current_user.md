# user_logout_current_user()

- **Type:** Function
- **File:** [`modules/user/user.pages.inc`](_file.md), lines 311–320 · [local source](../../../../source/modules/user/user.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc#L311-L320)
- **Module/theme:** user

## Signature

```php
function user_logout_current_user()
```

## Documentation

```text
Logs the current user out.
```

## Code

```php
function user_logout_current_user() {
  global $user;

  watchdog('user', 'Session closed for %name.', array('%name' => $user->name));

  module_invoke_all('user_logout', $user);

  // Destroy the current session, and reset $user to the anonymous user.
  session_destroy();
}
```

---
_Drupal 7.103 · [modules/user/user.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
