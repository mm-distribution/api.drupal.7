# trigger_user_view()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 541–544 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L541-L544)
- **Module/theme:** trigger
- **Implements:** [hook_user_view()](../../user/user.api.php/hook_user_view.md)

## Signature

```php
function trigger_user_view($account)
```

## Documentation

```text
Implements hook_user_view().
```

## Code

```php
function trigger_user_view($account) {
  $edit = NULL;
  _trigger_user('user_view', $edit, $account, NULL);
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
