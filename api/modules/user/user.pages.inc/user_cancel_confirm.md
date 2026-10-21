# user_cancel_confirm()

- **Type:** Function
- **File:** [`modules/user/user.pages.inc`](_file.md), lines 660–684 · [local source](../../../../source/modules/user/user.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc#L660-L684)
- **Module/theme:** user

## Signature

```php
function user_cancel_confirm($account, $timestamp = 0, $hashed_pass = '')
```

## Documentation

```text
Menu callback; Cancel a user account via e-mail confirmation link.

@see user_cancel_confirm_form()
@see user_cancel_url()
```

## Code

```php
function user_cancel_confirm($account, $timestamp = 0, $hashed_pass = '') {
  // Time out in seconds until cancel URL expires; 24 hours = 86400 seconds.
  $timeout = 86400;
  $current = REQUEST_TIME;

  // Basic validation of arguments.
  if (isset($account->data['user_cancel_method']) && !empty($timestamp) && !empty($hashed_pass)) {
    // Validate expiration and hashed password/login.
    if ($timestamp <= $current && $current - $timestamp < $timeout && $account->uid && $timestamp >= $account->login && $hashed_pass == user_pass_rehash($account->pass, $timestamp, $account->login, $account->uid, $account->mail)) {
      $edit = array(
        'user_cancel_notify' => isset($account->data['user_cancel_notify']) ? $account->data['user_cancel_notify'] : variable_get('user_mail_status_canceled_notify', FALSE),
      );
      user_cancel($edit, $account->uid, $account->data['user_cancel_method']);
      // Since user_cancel() is not invoked via Form API, batch processing needs
      // to be invoked manually and should redirect to the front page after
      // completion.
      batch_process('');
    }
    else {
      drupal_set_message(t('You have tried to use an account cancellation link that has expired. Please request a new one using the form below.'), 'error');
      drupal_goto("user/$account->uid/cancel");
    }
  }
  return MENU_ACCESS_DENIED;
}
```

---
_Drupal 7.103 · [modules/user/user.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
