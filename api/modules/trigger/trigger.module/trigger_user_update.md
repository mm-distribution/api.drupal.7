# trigger_user_update()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 515–517 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L515-L517)
- **Module/theme:** trigger
- **Implements:** [hook_user_update()](../../user/user.api.php/hook_user_update.md)

## Signature

```php
function trigger_user_update(&$edit, $account, $category)
```

## Documentation

```text
Implements hook_user_update().
```

## Code

```php
function trigger_user_update(&$edit, $account, $category) {
  _trigger_user('user_update', $edit, $account, $category);
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
