# user_user_flood_control()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 2269–2281 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L2269-L2281)
- **Module/theme:** user
- **Implements:** [hook_user_flood_control()](../user.api.php/hook_user_flood_control.md)

## Signature

```php
function user_user_flood_control($ip, $username = FALSE)
```

## Documentation

```text
Implements hook_user_flood_control().
```

## Code

```php
function user_user_flood_control($ip, $username = FALSE) {
  if (variable_get('log_user_flood_control', TRUE)) {
    if (!empty($username)) {
      watchdog('user', 'Flood control blocked login attempt for %user from %ip.', array(
        '%user' => $username,
        '%ip' => $ip
      ));
    }
    else {
      watchdog('user', 'Flood control blocked login attempt from %ip.', array('%ip' => $ip));
    }
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
