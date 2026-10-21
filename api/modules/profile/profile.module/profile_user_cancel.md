# profile_user_cancel()

- **Type:** Function
- **File:** [`modules/profile/profile.module`](_file.md), lines 232–239 · [local source](../../../../source/modules/profile/profile.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module#L232-L239)
- **Module/theme:** profile
- **Implements:** [hook_user_cancel()](../../user/user.api.php/hook_user_cancel.md)

## Signature

```php
function profile_user_cancel($edit, $account, $method)
```

## Documentation

```text
Implements hook_user_cancel().
```

## Code

```php
function profile_user_cancel($edit, $account, $method) {
  switch ($method) {
    case 'user_cancel_reassign':
      db_delete('profile_value')
        ->condition('uid', $account->uid)
        ->execute();
  }
}
```

---
_Drupal 7.103 · [modules/profile/profile.module](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module) · Licensed GPL-2.0-or-later (see LICENSE)._
