# user_user_operations_block()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 3333–3344 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L3333-L3344)
- **Module/theme:** user

## Signature

```php
function user_user_operations_block($accounts)
```

## Documentation

```text
Callback function for admin mass blocking users.
```

## Code

```php
function user_user_operations_block($accounts) {
  $accounts = user_load_multiple($accounts);
  foreach ($accounts as $account) {
    // Skip blocking user if they are already blocked.
    if ($account !== FALSE && $account->status == 1) {
      // For efficiency manually save the original account before applying any
      // changes.
      $account->original = clone $account;
      user_save($account, array('status' => 0));
    }
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
