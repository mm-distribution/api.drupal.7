# user_pass_validate()

- **Type:** Function
- **File:** [`modules/user/user.pages.inc`](_file.md), lines 68–110 · [local source](../../../../source/modules/user/user.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc#L68-L110)
- **Module/theme:** user

## Signature

```php
function user_pass_validate($form, &$form_state)
```

## Documentation

```text
Form validation handler for user_pass().

@see user_pass_submit()
```

## Code

```php
function user_pass_validate($form, &$form_state) {
  if (isset($form_state['values']['name']) && !is_scalar($form_state['values']['name'])) {
    form_set_error('name', t('An illegal value has been detected. Please contact the site administrator.'));
    return;
  }
  $user_pass_reset_ip_window = variable_get('user_pass_reset_ip_window', 3600);
  // Do not allow any password reset from the current user's IP if the limit
  // has been reached. Default is 50 attempts allowed in one hour. This is
  // independent of the per-user limit to catch attempts from one IP to request
  // resets for many different user accounts. We have a reasonably high limit
  // since there may be only one apparent IP for all users at an institution.
  if (!flood_is_allowed('pass_reset_ip', variable_get('user_pass_reset_ip_limit', 50), $user_pass_reset_ip_window)) {
    form_set_error('name', t('Sorry, too many password reset attempts from your IP address. This IP address is temporarily blocked. Try again later or <a href="@url">request a new password</a>.', array('@url' => url('user/password'))));
    return;
  }
  // Always register an per-IP event.
  flood_register_event('pass_reset_ip', $user_pass_reset_ip_window);
  $name = trim($form_state['values']['name']);
  // Try to load by email.
  $users = user_load_multiple(array(), array('mail' => $name, 'status' => '1'));
  $account = reset($users);
  if (!$account) {
    // No success, try to load by name.
    $users = user_load_multiple(array(), array('name' => $name, 'status' => '1'));
    $account = reset($users);
  }
  if (isset($account->uid)) {
    // Register user flood events based on the uid only, so they can be cleared
    // when a password is reset successfully.
    $identifier = $account->uid;
    $user_pass_reset_user_window = variable_get('user_pass_reset_user_window', 21600);
    $user_pass_reset_user_limit = variable_get('user_pass_reset_user_limit', 5);
    // Don't allow password reset if the limit for this user has been reached.
    // Default is to allow 5 passwords resets every 6 hours.
    if (!flood_is_allowed('pass_reset_user', $user_pass_reset_user_limit, $user_pass_reset_user_window, $identifier)) {
      form_set_error('name', format_plural($user_pass_reset_user_limit, 'Sorry, there has been more than one password reset attempt for this account. It is temporarily blocked. Try again later or <a href="@url">login with your password</a>.', 'Sorry, there have been more than @count password reset attempts for this account. It is temporarily blocked. Try again later or <a href="@url">login with your password</a>.', array('@url' => url('user/login'))));
      return;
    }
    // Register a per-user event.
    flood_register_event('pass_reset_user', $user_pass_reset_user_window, $identifier);
    form_set_value(array('#parents' => array('account')), $account, $form_state);
  }
}
```

---
_Drupal 7.103 · [modules/user/user.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
