# _profile_update_user_fields()

- **Type:** Function
- **File:** [`modules/profile/profile.module`](_file.md), lines 472–477 · [local source](../../../../source/modules/profile/profile.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module#L472-L477)
- **Module/theme:** profile

## Signature

```php
function _profile_update_user_fields($fields, $account)
```

## Documentation

```text
Helper function: update an array of user fields by calling profile_view_field
```

## Code

```php
function _profile_update_user_fields($fields, $account) {
  foreach ($fields as $key => $field) {
    $fields[$key]->value = profile_view_field($account, $field);
  }
  return $fields;
}
```

---
_Drupal 7.103 · [modules/profile/profile.module](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module) · Licensed GPL-2.0-or-later (see LICENSE)._
