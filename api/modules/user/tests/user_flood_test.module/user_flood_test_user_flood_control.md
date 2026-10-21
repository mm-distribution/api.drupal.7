# user_flood_test_user_flood_control()

- **Type:** Function
- **File:** [`modules/user/tests/user_flood_test.module`](_file.md), lines 11–18 · [local source](../../../../../source/modules/user/tests/user_flood_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/tests/user_flood_test.module#L11-L18)
- **Module/theme:** user_flood_test
- **Implements:** [hook_user_flood_control()](../../user.api.php/hook_user_flood_control.md)

## Signature

```php
function user_flood_test_user_flood_control($ip, $username = FALSE)
```

## Documentation

```text
Implements hook_user_flood_control().
```

## Code

```php
function user_flood_test_user_flood_control($ip, $username = FALSE) {
  if (!empty($username)) {
    watchdog('user_flood_test', 'hook_user_flood_control was passed username %username and IP %ip.', array('%username' => $username, '%ip' => $ip));
  }
  else {
    watchdog('user_flood_test', 'hook_user_flood_control was passed IP %ip.', array('%ip' => $ip));
  }
}
```

---
_Drupal 7.103 · [modules/user/tests/user_flood_test.module](https://github.com/drupal/drupal/blob/7.103/modules/user/tests/user_flood_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
