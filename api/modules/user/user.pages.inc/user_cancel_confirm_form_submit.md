# user_cancel_confirm_form_submit()

- **Type:** Function
- **File:** [`modules/user/user.pages.inc`](_file.md), lines 575–601 · [local source](../../../../source/modules/user/user.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc#L575-L601)
- **Module/theme:** user

## Signature

```php
function user_cancel_confirm_form_submit($form, &$form_state)
```

## Documentation

```text
Submit handler for the account cancellation confirm form.

@see user_cancel_confirm_form()
@see user_multiple_cancel_confirm_submit()
```

## Code

```php
function user_cancel_confirm_form_submit($form, &$form_state) {
  global $user;
  $account = $form_state['values']['_account'];

  // Cancel account immediately, if the current user has administrative
  // privileges, no confirmation mail shall be sent, and the user does not
  // attempt to cancel the own account.
  if (user_access('administer users') && empty($form_state['values']['user_cancel_confirm']) && $account->uid != $user->uid) {
    user_cancel($form_state['values'], $account->uid, $form_state['values']['user_cancel_method']);

    $form_state['redirect'] = 'admin/people';
  }
  else {
    // Store cancelling method and whether to notify the user in $account for
    // user_cancel_confirm().
    $edit = array(
      'user_cancel_method' => $form_state['values']['user_cancel_method'],
      'user_cancel_notify' => $form_state['values']['user_cancel_notify'],
    );
    $account = user_save($account, $edit);
    _user_mail_notify('cancel_confirm', $account);
    drupal_set_message(t('A confirmation request to cancel your account has been sent to your e-mail address.'));
    watchdog('user', 'Sent account cancellation request to %name %email.', array('%name' => $account->name, '%email' => '<' . $account->mail . '>'), WATCHDOG_NOTICE);

    $form_state['redirect'] = "user/$account->uid";
  }
}
```

---
_Drupal 7.103 · [modules/user/user.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
