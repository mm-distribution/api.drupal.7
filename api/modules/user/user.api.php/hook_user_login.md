# hook_user_login()

- **Type:** Hook (documentation function)
- **File:** [`modules/user/user.api.php`](_file.md), lines 310–315 · [local source](../../../../source/modules/user/user.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.api.php#L310-L315)
- **Module/theme:** user
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_user_login(&$form_state, $account)
```

## Documentation

```text
The user just logged in.

@param $form_state
  A keyed array containing the current state of the login form.
@param $account
  The user object on which the operation was just performed.
```

## Code

```php
function hook_user_login(&$form_state, $account) {
  // If the user has a NULL time zone, notify them to set a time zone.
  if (!$account->timezone && variable_get('configurable_timezones', 1) && variable_get('empty_timezone_message', 0)) {
    drupal_set_message(t('Configure your <a href="@user-edit">account time zone setting</a>.', array('@user-edit' => url("user/$account->uid/edit", array('query' => drupal_get_destination(), 'fragment' => 'edit-timezone')))));
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_user_login()".

- [openid_user_login()](../../openid/openid.module/openid_user_login.md) — `modules/openid/openid.module`
- [system_user_login()](../../system/system.module/system_user_login.md) — `modules/system/system.module`
- [trigger_user_login()](../../trigger/trigger.module/trigger_user_login.md) — `modules/trigger/trigger.module`

---
_Drupal 7.103 · [modules/user/user.api.php](https://github.com/drupal/drupal/blob/7.103/modules/user/user.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
