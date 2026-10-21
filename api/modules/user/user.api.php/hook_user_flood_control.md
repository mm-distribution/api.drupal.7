# hook_user_flood_control()

- **Type:** Hook (documentation function)
- **File:** [`modules/user/user.api.php`](_file.md), lines 489–503 · [local source](../../../../source/modules/user/user.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.api.php#L489-L503)
- **Module/theme:** user
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_user_flood_control($ip, $username = FALSE)
```

## Documentation

```text
Respond to user flood control events.

This hook allows you act when an unsuccessful user login has triggered
flood control. This means that either an IP address or a specific user
account has been temporarily blocked from logging in.

@param $ip
  The IP address that triggered flood control.
@param $username
  The username that has been temporarily blocked.

@see user_login_final_validate()
```

## Code

```php
function hook_user_flood_control($ip, $username = FALSE) {
  if (!empty($username)) {
    // Do something with the blocked $username and $ip. For example, send an
    // e-mail to the user and/or site administrator.

    // Drupal core uses this hook to log the event:
    watchdog('user', 'Flood control blocked login attempt for %user from %ip.', array('%user' => $username, '%ip' => $ip));
  }
  else {
    // Do something with the blocked $ip. For example, add it to a block-list.

    // Drupal core uses this hook to log the event:
    watchdog('user', 'Flood control blocked login attempt from %ip.', array('%ip' => $ip));
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_user_flood_control()".

- [user_user_flood_control()](../user.module/user_user_flood_control.md) — `modules/user/user.module`
- [user_flood_test_user_flood_control()](../tests/user_flood_test.module/user_flood_test_user_flood_control.md) — `modules/user/tests/user_flood_test.module`

---
_Drupal 7.103 · [modules/user/user.api.php](https://github.com/drupal/drupal/blob/7.103/modules/user/user.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
