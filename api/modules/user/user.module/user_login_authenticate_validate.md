# user_login_authenticate_validate()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 2183–2221 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L2183-L2221)
- **Module/theme:** user

## Signature

```php
function user_login_authenticate_validate($form, &$form_state)
```

## Documentation

```text
A validate handler on the login form. Check supplied username/password
against local users table. If successful, $form_state['uid']
is set to the matching user ID.
```

## Code

```php
function user_login_authenticate_validate($form, &$form_state) {
  $password = trim($form_state['values']['pass']);
  if (!empty($form_state['values']['name']) && strlen(trim($password)) > 0) {
    // Do not allow any login from the current user's IP if the limit has been
    // reached. Default is 50 failed attempts allowed in one hour. This is
    // independent of the per-user limit to catch attempts from one IP to log
    // in to many different user accounts.  We have a reasonably high limit
    // since there may be only one apparent IP for all users at an institution.
    if (!flood_is_allowed('failed_login_attempt_ip', variable_get('user_failed_login_ip_limit', 50), variable_get('user_failed_login_ip_window', 3600))) {
      $form_state['flood_control_triggered'] = 'ip';
      return;
    }
    $account = db_query("SELECT * FROM {users} WHERE name = :name AND status = 1", array(':name' => $form_state['values']['name']))->fetchObject();
    if ($account) {
      if (variable_get('user_failed_login_identifier_uid_only', FALSE)) {
        // Register flood events based on the uid only, so they apply for any
        // IP address. This is the most secure option.
        $identifier = $account->uid;
      }
      else {
        // The default identifier is a combination of uid and IP address. This
        // is less secure but more resistant to denial-of-service attacks that
        // could lock out all users with public user names.
        $identifier = $account->uid . '-' . ip_address();
      }
      $form_state['flood_control_user_identifier'] = $identifier;

      // Don't allow login if the limit for this user has been reached.
      // Default is to allow 5 failed attempts every 6 hours.
      if (!flood_is_allowed('failed_login_attempt_user', variable_get('user_failed_login_user_limit', 5), variable_get('user_failed_login_user_window', 21600), $identifier)) {
        $form_state['flood_control_triggered'] = 'user';
        return;
      }
    }
    // We are not limited by flood control, so try to authenticate.
    // Set $form_state['uid'] as a flag for user_login_final_validate().
    $form_state['uid'] = user_authenticate($form_state['values']['name'], $password);
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
