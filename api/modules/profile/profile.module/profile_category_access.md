# profile_category_access()

- **Type:** Function
- **File:** [`modules/profile/profile.module`](_file.md), lines 519–530 · [local source](../../../../source/modules/profile/profile.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module#L519-L530)
- **Module/theme:** profile

## Signature

```php
function profile_category_access($account, $category)
```

## Documentation

```text
Menu item access callback - check if a user has access to a profile category.
```

## Code

```php
function profile_category_access($account, $category) {
  if (user_access('administer users') && $account->uid > 0) {
    return TRUE;
  }
  else {
    $category_visible = (bool) db_query_range('SELECT 1 FROM {profile_field} WHERE category = :category AND visibility <> :visibility', 0, 1, array(
      ':category' => $category,
      ':visibility' => PROFILE_HIDDEN
    ))->fetchField();
    return user_edit_access($account) && $category_visible;
  }
}
```

---
_Drupal 7.103 · [modules/profile/profile.module](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module) · Licensed GPL-2.0-or-later (see LICENSE)._
