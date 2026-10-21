# profile_user_insert()

- **Type:** Function
- **File:** [`modules/profile/profile.module`](_file.md), lines 225–227 · [local source](../../../../source/modules/profile/profile.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module#L225-L227)
- **Module/theme:** profile
- **Implements:** [hook_user_insert()](../../user/user.api.php/hook_user_insert.md)

## Signature

```php
function profile_user_insert(&$edit, $account, $category)
```

## Documentation

```text
Implements hook_user_insert().
```

## Code

```php
function profile_user_insert(&$edit, $account, $category) {
  profile_save_profile($edit, $account, $category, TRUE);
}
```

---
_Drupal 7.103 · [modules/profile/profile.module](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module) · Licensed GPL-2.0-or-later (see LICENSE)._
