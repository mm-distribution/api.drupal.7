# user_user_operations_unblock()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 3320–3328 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L3320-L3328)
- **Module/theme:** user

## Signature

```php
function user_user_operations_unblock($accounts)
```

## Documentation

```text
Callback function for admin mass unblocking users.
```

## Code

```php
function user_user_operations_unblock($accounts) {
  $accounts = user_load_multiple($accounts);
  foreach ($accounts as $account) {
    // Skip unblocking user if they are already unblocked.
    if ($account !== FALSE && $account->status == 0) {
      user_save($account, array('status' => 1));
    }
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
