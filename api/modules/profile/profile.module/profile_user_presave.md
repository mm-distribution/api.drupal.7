# profile_user_presave()

- **Type:** Function
- **File:** [`modules/profile/profile.module`](_file.md), lines 216–220 · [local source](../../../../source/modules/profile/profile.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module#L216-L220)
- **Module/theme:** profile
- **Implements:** [hook_user_presave()](../../user/user.api.php/hook_user_presave.md)

## Signature

```php
function profile_user_presave(&$edit, $account, $category)
```

## Documentation

```text
Implements hook_user_presave().
```

## Code

```php
function profile_user_presave(&$edit, $account, $category) {
  if (!empty($account->uid)) {
    profile_save_profile($edit, $account, $category);
  }
}
```

---
_Drupal 7.103 · [modules/profile/profile.module](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module) · Licensed GPL-2.0-or-later (see LICENSE)._
