# trigger_user_cancel()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 522–528 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L522-L528)
- **Module/theme:** trigger
- **Implements:** [hook_user_cancel()](../../user/user.api.php/hook_user_cancel.md)

## Signature

```php
function trigger_user_cancel($edit, $account, $method)
```

## Documentation

```text
Implements hook_user_cancel().
```

## Code

```php
function trigger_user_cancel($edit, $account, $method) {
  switch ($method) {
    case 'user_cancel_reassign':
      _trigger_user('user_delete', $edit, $account, $method);
      break;
  }
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
