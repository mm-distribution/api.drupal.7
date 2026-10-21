# profile_user_categories()

- **Type:** Function
- **File:** [`modules/profile/profile.module`](_file.md), lines 501–514 · [local source](../../../../source/modules/profile/profile.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module#L501-L514)
- **Module/theme:** profile
- **Implements:** [hook_user_categories()](../../user/user.api.php/hook_user_categories.md)

## Signature

```php
function profile_user_categories()
```

## Documentation

```text
Implements hook_user_categories().
```

## Code

```php
function profile_user_categories() {
  $result = db_query("SELECT DISTINCT(category) FROM {profile_field}");
  $data = array();
  foreach ($result as $category) {
    $data[] = array(
      'name' => $category->category,
      'title' => $category->category,
      'weight' => 3,
      'access callback' => 'profile_category_access',
      'access arguments' => array(1, $category->category)
    );
  }
  return $data;
}
```

---
_Drupal 7.103 · [modules/profile/profile.module](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module) · Licensed GPL-2.0-or-later (see LICENSE)._
