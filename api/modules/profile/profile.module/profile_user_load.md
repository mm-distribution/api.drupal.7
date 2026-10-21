# profile_user_load()

- **Type:** Function
- **File:** [`modules/profile/profile.module`](_file.md), lines 253–260 · [local source](../../../../source/modules/profile/profile.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module#L253-L260)
- **Module/theme:** profile
- **Implements:** [hook_user_load()](../../user/user.api.php/hook_user_load.md)

## Signature

```php
function profile_user_load($users)
```

## Documentation

```text
Implements hook_user_load().
```

## Code

```php
function profile_user_load($users) {
  $result = db_query('SELECT f.name, f.type, v.uid, v.value FROM {profile_field} f INNER JOIN {profile_value} v ON f.fid = v.fid WHERE uid IN (:uids)', array(':uids' => array_keys($users)));
  foreach ($result as $record) {
    if (empty($users[$record->uid]->{$record->name})) {
      $users[$record->uid]->{$record->name} = _profile_field_serialize($record->type) ? unserialize($record->value) : $record->value;
    }
  }
}
```

---
_Drupal 7.103 · [modules/profile/profile.module](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module) · Licensed GPL-2.0-or-later (see LICENSE)._
