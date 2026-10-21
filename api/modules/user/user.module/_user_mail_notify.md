# _user_mail_notify()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 3669–3684 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L3669-L3684)
- **Module/theme:** user

## Signature

```php
function _user_mail_notify($op, $account, $language = NULL)
```

## Documentation

```text
Conditionally create and send a notification email when a certain
operation happens on the given user account.

@see user_mail_tokens()
@see drupal_mail()

@param $op
  The operation being performed on the account. Possible values:
  - 'register_admin_created': Welcome message for user created by the admin.
  - 'register_no_approval_required': Welcome message when user
    self-registers.
  - 'register_pending_approval': Welcome message, user pending admin
    approval.
  - 'password_reset': Password recovery request.
  - 'status_activated': Account activated.
  - 'status_blocked': Account blocked.
  - 'cancel_confirm': Account cancellation request.
  - 'status_canceled': Account canceled.

@param $account
  The user object of the account being notified. Must contain at
  least the fields 'uid', 'name', and 'mail'.
@param $language
  Optional language to use for the notification, overriding account language.

@return
  The return value from drupal_mail_system()->mail(), if ends up being
  called.
```

## Code

```php
function _user_mail_notify($op, $account, $language = NULL) {
  // By default, we always notify except for canceled and blocked.
  $default_notify = ($op != 'status_canceled' && $op != 'status_blocked');
  $notify = variable_get('user_mail_' . $op . '_notify', $default_notify);
  if ($notify) {
    $params['account'] = $account;
    $language = $language ? $language : user_preferred_language($account);
    $mail = drupal_mail('user', $op, $account->mail, $language, $params);
    if ($op == 'register_pending_approval') {
      // If a user registered requiring admin approval, notify the admin, too.
      // We use the site default language for this.
      drupal_mail('user', 'register_pending_approval_admin', variable_get('site_mail', ini_get('sendmail_from')), language_default(), $params);
    }
  }
  return empty($mail) ? NULL : $mail['result'];
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
