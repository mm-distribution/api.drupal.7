# profile_save_profile()

- **Type:** Function
- **File:** [`modules/profile/profile.module`](_file.md), lines 262–276 · [local source](../../../../source/modules/profile/profile.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module#L262-L276)
- **Module/theme:** profile

## Signature

```php
function profile_save_profile(&$edit, $account, $category, $register = FALSE)
```

## Documentation

_No docblock in source._

## Code

```php
function profile_save_profile(&$edit, $account, $category, $register = FALSE) {
  $result = _profile_get_fields($category, $register);
  foreach ($result as $field) {
    if (_profile_field_serialize($field->type)) {
      $edit[$field->name] = serialize($edit[$field->name]);
    }
    db_merge('profile_value')
      ->key(array(
        'fid' => $field->fid,
        'uid' => $account->uid,
      ))
      ->fields(array('value' => $edit[$field->name]))
      ->execute();
  }
}
```

---
_Drupal 7.103 · [modules/profile/profile.module](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module) · Licensed GPL-2.0-or-later (see LICENSE)._
