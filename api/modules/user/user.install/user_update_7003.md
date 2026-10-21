# user_update_7003()

- **Type:** Function
- **File:** [`modules/user/user.install`](_file.md), lines 565–582 · [local source](../../../../source/modules/user/user.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install#L565-L582)
- **Module/theme:** user
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function user_update_7003()
```

## Documentation

```text
Update user settings for cancelling user accounts.

Prior to 7.x, users were not able to cancel their accounts. When
administrators deleted an account, all contents were assigned to uid 0,
which is the same as the 'user_cancel_reassign' method now.
```

## Code

```php
function user_update_7003() {
  // Set the default account cancellation method.
  variable_set('user_cancel_method', 'user_cancel_reassign');
  // Re-assign notification setting.
  if ($setting = variable_get('user_mail_status_deleted_notify', FALSE)) {
    variable_set('user_mail_status_canceled_notify', $setting);
    variable_del('user_mail_status_deleted_notify');
  }
  // Re-assign "Account deleted" mail strings to "Account canceled" mail.
  if ($setting = variable_get('user_mail_status_deleted_subject', FALSE)) {
    variable_set('user_mail_status_canceled_subject', $setting);
    variable_del('user_mail_status_deleted_subject');
  }
  if ($setting = variable_get('user_mail_status_deleted_body', FALSE)) {
    variable_set('user_mail_status_canceled_body', $setting);
    variable_del('user_mail_status_deleted_body');
  }
}
```

---
_Drupal 7.103 · [modules/user/user.install](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install) · Licensed GPL-2.0-or-later (see LICENSE)._
