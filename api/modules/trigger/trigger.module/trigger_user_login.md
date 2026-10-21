# trigger_user_login()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 493–495 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L493-L495)
- **Module/theme:** trigger
- **Implements:** [hook_user_login()](../../user/user.api.php/hook_user_login.md)

## Signature

```php
function trigger_user_login(&$edit, $account, $category)
```

## Documentation

```text
Implements hook_user_login().
```

## Code

```php
function trigger_user_login(&$edit, $account, $category) {
  _trigger_user('user_login', $edit, $account, $category);
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
