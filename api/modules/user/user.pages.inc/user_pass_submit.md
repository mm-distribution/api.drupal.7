# user_pass_submit()

- **Type:** Function
- **File:** [`modules/user/user.pages.inc`](_file.md), lines 117–137 · [local source](../../../../source/modules/user/user.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc#L117-L137)
- **Module/theme:** user

## Signature

```php
function user_pass_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for user_pass().

@see user_pass_validate()
```

## Code

```php
function user_pass_submit($form, &$form_state) {
  global $language;

  $name = $form_state['values']['name'];
  if (isset($form_state['values']['account'])) {
    $account = $form_state['values']['account'];
    // Mail one time login URL and instructions using current language.
    $mail = _user_mail_notify('password_reset', $account, $language);
    if (!empty($mail)) {
      watchdog('user', 'Password reset instructions mailed to %name at %email.', array('%name' => $account->name, '%email' => $account->mail));
    }
  }
  else {
    watchdog('user', 'Password reset form was submitted with an unknown or inactive account: %name.', array('%name' => $name));
  }

  $password_reset_text = variable_get('user_password_reset_text', t('If %identifier is a valid account, an email will be sent with instructions to reset your password.'));
  drupal_set_message(format_string($password_reset_text, array('%identifier' => $name)));
  $form_state['redirect'] = 'user';
  return;
}
```

---
_Drupal 7.103 · [modules/user/user.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
