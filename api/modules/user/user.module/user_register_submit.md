# user_register_submit()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 3980–4051 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L3980-L4051)
- **Module/theme:** user

## Signature

```php
function user_register_submit($form, &$form_state)
```

## Documentation

```text
Submit handler for the user registration form.

This function is shared by the installation form and the normal registration form,
which is why it can't be in the user.pages.inc file.

@see user_register_form()
```

## Code

```php
function user_register_submit($form, &$form_state) {
  $admin = $form_state['values']['administer_users'];

  if (!variable_get('user_email_verification', TRUE) || $admin) {
    $pass = $form_state['values']['pass'];
  }
  else {
    $pass = user_password();
  }
  $notify = !empty($form_state['values']['notify']);

  // Remove unneeded values.
  form_state_values_clean($form_state);

  $form_state['values']['pass'] = $pass;
  $form_state['values']['init'] = $form_state['values']['mail'];

  $account = $form['#user'];

  entity_form_submit_build_entity('user', $account, $form, $form_state);

  // Populate $edit with the properties of $account, which have been edited on
  // this form by taking over all values, which appear in the form values too.
  $edit = array_intersect_key((array) $account, $form_state['values']);
  $account = user_save($account, $edit);

  // Terminate if an error occurred during user_save().
  if (!$account) {
    drupal_set_message(t("Error saving user account."), 'error');
    $form_state['redirect'] = '';
    return;
  }
  $form_state['user'] = $account;
  $form_state['values']['uid'] = $account->uid;

  watchdog('user', 'New user: %name (%email).', array('%name' => $form_state['values']['name'], '%email' => $form_state['values']['mail']), WATCHDOG_NOTICE, l(t('edit'), 'user/' . $account->uid . '/edit'));

  // Add plain text password into user account to generate mail tokens.
  $account->password = $pass;

  // New administrative account without notification.
  $uri = entity_uri('user', $account);
  if ($admin && !$notify) {
    drupal_set_message(t('Created a new user account for <a href="@url">%name</a>. No e-mail has been sent.', array('@url' => url($uri['path'], $uri['options']), '%name' => $account->name)));
  }
  // No e-mail verification required; log in user immediately.
  elseif (!$admin && !variable_get('user_email_verification', TRUE) && $account->status) {
    _user_mail_notify('register_no_approval_required', $account);
    $form_state['uid'] = $account->uid;
    user_login_submit(array(), $form_state);
    drupal_set_message(t('Registration successful. You are now logged in.'));
    $form_state['redirect'] = '';
  }
  // No administrator approval required.
  elseif ($account->status || $notify) {
    $op = $notify ? 'register_admin_created' : 'register_no_approval_required';
    _user_mail_notify($op, $account);
    if ($notify) {
      drupal_set_message(t('A welcome message with further instructions has been e-mailed to the new user <a href="@url">%name</a>.', array('@url' => url($uri['path'], $uri['options']), '%name' => $account->name)));
    }
    else {
      drupal_set_message(t('A welcome message with further instructions has been sent to your e-mail address.'));
      $form_state['redirect'] = '';
    }
  }
  // Administrator approval required.
  else {
    _user_mail_notify('register_pending_approval', $account);
    drupal_set_message(t('Thank you for applying for an account. Your account is currently pending approval by the site administrator.<br />In the meantime, a welcome message with further instructions has been sent to your e-mail address.'));
    $form_state['redirect'] = '';
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
