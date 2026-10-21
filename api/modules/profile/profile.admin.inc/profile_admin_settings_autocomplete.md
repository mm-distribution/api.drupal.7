# profile_admin_settings_autocomplete()

- **Type:** Function
- **File:** [`modules/profile/profile.admin.inc`](_file.md), lines 434–446 · [local source](../../../../source/modules/profile/profile.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.admin.inc#L434-L446)
- **Module/theme:** profile

## Signature

```php
function profile_admin_settings_autocomplete($string)
```

## Documentation

```text
Retrieve a pipe delimited string of autocomplete suggestions for profile categories
```

## Code

```php
function profile_admin_settings_autocomplete($string) {
  $matches = array();
  $result = db_select('profile_field')
    ->fields('profile_field', array('category'))
    ->condition('category', db_like($string) . '%', 'LIKE')
    ->range(0, 10)
    ->execute();

  foreach ($result as $data) {
    $matches[$data->category] = check_plain($data->category);
  }
  drupal_json_output($matches);
}
```

---
_Drupal 7.103 · [modules/profile/profile.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
