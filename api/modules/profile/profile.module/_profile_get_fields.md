# _profile_get_fields()

- **Type:** Function
- **File:** [`modules/profile/profile.module`](_file.md), lines 614–630 · [local source](../../../../source/modules/profile/profile.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module#L614-L630)
- **Module/theme:** profile

## Signature

```php
function _profile_get_fields($category, $register = FALSE)
```

## Documentation

_No docblock in source._

## Code

```php
function _profile_get_fields($category, $register = FALSE) {
  $query = db_select('profile_field');
  if ($register) {
    $query->condition('register', 1);
  }
  else {
    $query->condition('category', db_like($category), 'LIKE');
  }
  if (!user_access('administer users')) {
    $query->condition('visibility', PROFILE_HIDDEN, '<>');
  }
  return $query
    ->fields('profile_field')
    ->orderBy('category', 'ASC')
    ->orderBy('weight', 'ASC')
    ->execute();
}
```

---
_Drupal 7.103 · [modules/profile/profile.module](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module) · Licensed GPL-2.0-or-later (see LICENSE)._
