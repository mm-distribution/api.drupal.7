# profile_user_delete()

- **Type:** Function
- **File:** [`modules/profile/profile.module`](_file.md), lines 244–248 · [local source](../../../../source/modules/profile/profile.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module#L244-L248)
- **Module/theme:** profile
- **Implements:** [hook_user_delete()](../../user/user.api.php/hook_user_delete.md)

## Signature

```php
function profile_user_delete($account)
```

## Documentation

```text
Implements hook_user_delete().
```

## Code

```php
function profile_user_delete($account) {
  db_delete('profile_value')
    ->condition('uid', $account->uid)
    ->execute();
}
```

---
_Drupal 7.103 · [modules/profile/profile.module](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module) · Licensed GPL-2.0-or-later (see LICENSE)._
