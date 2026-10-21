# trigger_user_delete()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 533–536 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L533-L536)
- **Module/theme:** trigger
- **Implements:** [hook_user_delete()](../../user/user.api.php/hook_user_delete.md)

## Signature

```php
function trigger_user_delete($account)
```

## Documentation

```text
Implements hook_user_delete().
```

## Code

```php
function trigger_user_delete($account) {
  $edit = array();
  _trigger_user('user_delete', $edit, $account, NULL);
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
