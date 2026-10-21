# trigger_user_insert()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 508–510 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L508-L510)
- **Module/theme:** trigger
- **Implements:** [hook_user_insert()](../../user/user.api.php/hook_user_insert.md)

## Signature

```php
function trigger_user_insert(&$edit, $account, $category)
```

## Documentation

```text
Implements hook_user_insert().
```

## Code

```php
function trigger_user_insert(&$edit, $account, $category) {
  _trigger_user('user_insert', $edit, $account, $category);
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
