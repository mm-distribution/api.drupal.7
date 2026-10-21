# trigger_user_logout()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 500–503 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L500-L503)
- **Module/theme:** trigger
- **Implements:** [hook_user_logout()](../../user/user.api.php/hook_user_logout.md)

## Signature

```php
function trigger_user_logout($account)
```

## Documentation

```text
Implements hook_user_logout().
```

## Code

```php
function trigger_user_logout($account) {
  $edit = array();
  _trigger_user('user_logout', $edit, $account);
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
