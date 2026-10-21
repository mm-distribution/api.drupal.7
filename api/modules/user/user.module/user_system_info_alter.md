# user_system_info_alter()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 4167–4171 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L4167-L4171)
- **Module/theme:** user
- **Implements:** [hook_system_info_alter()](../../system/system.api.php/hook_system_info_alter.md)

## Signature

```php
function user_system_info_alter(&$info, $file, $type)
```

## Documentation

```text
Implements hook_system_info_alter().

Drupal 7 ships with two methods to add additional fields to users: Profile
module, a legacy module dating back from 2002, and Field API integration
with users. While Field API support for users currently provides less end
user features, the inefficient data storage mechanism of Profile module, as
well as its lack of consistency with the rest of the entity / field based
systems in Drupal 7, make this a sub-optimal solution to those who were not
using it in previous releases of Drupal.

To prevent new Drupal 7 sites from installing Profile module, and
unwittingly ending up with two completely different and incompatible methods
of extending users, only make the Profile module available if the profile_*
tables are present.

@todo: Remove in D8, pending upgrade path.
```

## Code

```php
function user_system_info_alter(&$info, $file, $type) {
  if ($type == 'module' && $file->name == 'profile' && db_table_exists('profile_field')) {
    $info['hidden'] = FALSE;
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
