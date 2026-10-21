# system_user_login()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 2029–2034 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L2029-L2034)
- **Module/theme:** system
- **Implements:** [hook_user_login()](../../user/user.api.php/hook_user_login.md)

## Signature

```php
function system_user_login(&$edit, $account)
```

## Documentation

```text
Implements hook_user_login().
```

## Code

```php
function system_user_login(&$edit, $account) {
  // If the user has a NULL time zone, notify them to set a time zone.
  if (!$account->timezone && variable_get('configurable_timezones', 1) && variable_get('empty_timezone_message', 0)) {
    drupal_set_message(t('Configure your <a href="@user-edit">account time zone setting</a>.', array('@user-edit' => url("user/$account->uid/edit", array('query' => drupal_get_destination(), 'fragment' => 'edit-timezone')))));
  }
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
