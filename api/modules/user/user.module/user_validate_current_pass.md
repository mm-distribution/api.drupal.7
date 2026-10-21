# user_validate_current_pass()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 1237–1254 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L1237-L1254)
- **Module/theme:** user

## Signature

```php
function user_validate_current_pass(&$form, &$form_state)
```

## Documentation

```text
Form validation handler for the current password on the user_account_form().

@see user_account_form()
```

## Code

```php
function user_validate_current_pass(&$form, &$form_state) {
  $account = $form['#user'];
  foreach ($form_state['values']['current_pass_required_values'] as $key => $name) {
    // This validation only works for required textfields (like mail) or
    // form values like password_confirm that have their own validation
    // that prevent them from being empty if they are changed.
    if ((strlen(trim($form_state['values'][$key])) > 0) && ($form_state['values'][$key] != $account->$key)) {
      require_once DRUPAL_ROOT . '/' . variable_get('password_inc', 'includes/password.inc');
      $current_pass_failed = strlen(trim($form_state['values']['current_pass'])) == 0 || !user_check_password($form_state['values']['current_pass'], $account);
      if ($current_pass_failed) {
        form_set_error('current_pass', t("Your current password is missing or incorrect; it's required to change the %name.", array('%name' => $name)));
        form_set_error($key);
      }
      // We only need to check the password once.
      break;
    }
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
