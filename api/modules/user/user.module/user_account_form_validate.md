# user_account_form_validate()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 1261–1312 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L1261-L1312)
- **Module/theme:** user

## Signature

```php
function user_account_form_validate($form, &$form_state)
```

## Documentation

```text
Form validation handler for user_account_form().

@see user_account_form()
```

## Code

```php
function user_account_form_validate($form, &$form_state) {
  if ($form['#user_category'] == 'account' || $form['#user_category'] == 'register') {
    $account = $form['#user'];
    // Validate new or changing username.
    if (isset($form_state['values']['name'])) {
      if ($error = user_validate_name($form_state['values']['name'])) {
        form_set_error('name', $error);
      }
      elseif ((bool) db_select('users')->fields('users', array('uid'))->condition('uid', $account->uid, '<>')->condition('name', db_like($form_state['values']['name']), 'LIKE')->range(0, 1)->execute()->fetchField()) {
        form_set_error('name', t('The name %name is already taken.', array('%name' => $form_state['values']['name'])));
      }
    }

    // Trim whitespace from mail, to prevent confusing 'e-mail not valid'
    // warnings often caused by cutting and pasting.
    $mail = trim($form_state['values']['mail']);
    form_set_value($form['account']['mail'], $mail, $form_state);

    // Validate the e-mail address, and check if it is taken by an existing user.
    if ($error = user_validate_mail($form_state['values']['mail'])) {
      form_set_error('mail', $error);
    }
    elseif ((bool) db_select('users')->fields('users', array('uid'))->condition('uid', $account->uid, '<>')->condition('mail', db_like($form_state['values']['mail']), 'LIKE')->range(0, 1)->execute()->fetchField()) {
      // Format error message dependent on whether the user is logged in or not.
      if ($GLOBALS['user']->uid) {
        // Do not fail the validation if user has not changed e-mail address.
        // This means that multiple accounts with the same e-mail address exist
        // and the logged-in user is one of them.
        if ((isset($account->mail) && $account->mail != $mail) || !isset($account->mail)) {
          form_set_error('mail', t('The e-mail address %email is already taken.', array('%email' => $form_state['values']['mail'])));
        }
      }
      else {
        form_set_error('mail', t('The e-mail address %email is already registered. <a href="@password">Have you forgotten your password?</a>', array('%email' => $form_state['values']['mail'], '@password' => url('user/password'))));
      }
    }

    // Make sure the signature isn't longer than the size of the database field.
    // Signatures are disabled by default, so make sure it exists first.
    if (isset($form_state['values']['signature'])) {
      // Move text format for user signature into 'signature_format'.
      $form_state['values']['signature_format'] = $form_state['values']['signature']['format'];
      // Move text value for user signature into 'signature'.
      $form_state['values']['signature'] = $form_state['values']['signature']['value'];

      $user_schema = drupal_get_schema('users');
      if (drupal_strlen($form_state['values']['signature']) > $user_schema['fields']['signature']['length']) {
        form_set_error('signature', t('The signature is too long: it must be %max characters or less.', array('%max' => $user_schema['fields']['signature']['length'])));
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
