# user_multiple_cancel_confirm()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 3384–3446 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L3384-L3446)
- **Module/theme:** user

## Signature

```php
function user_multiple_cancel_confirm($form, &$form_state)
```

## Documentation

_No docblock in source._

## Code

```php
function user_multiple_cancel_confirm($form, &$form_state) {
  $edit = $form_state['input'];

  $form['accounts'] = array('#prefix' => '<ul>', '#suffix' => '</ul>', '#tree' => TRUE);
  $accounts = user_load_multiple(array_keys(array_filter($edit['accounts'])));
  foreach ($accounts as $uid => $account) {
    // Prevent user 1 from being canceled.
    if ($uid <= 1) {
      continue;
    }
    $form['accounts'][$uid] = array(
      '#type' => 'hidden',
      '#value' => $uid,
      '#prefix' => '<li>',
      '#suffix' => check_plain($account->name) . "</li>\n",
    );
  }

  // Output a notice that user 1 cannot be canceled.
  if (isset($accounts[1])) {
    $redirect = (count($accounts) == 1);
    $message = t('The user account %name cannot be cancelled.', array('%name' => $accounts[1]->name));
    drupal_set_message($message, $redirect ? 'error' : 'warning');
    // If only user 1 was selected, redirect to the overview.
    if ($redirect) {
      drupal_goto('admin/people');
    }
  }

  $form['operation'] = array('#type' => 'hidden', '#value' => 'cancel');

  module_load_include('inc', 'user', 'user.pages');
  $form['user_cancel_method'] = array(
    '#type' => 'item',
    '#title' => t('When cancelling these accounts'),
  );
  $form['user_cancel_method'] += user_cancel_methods();
  // Remove method descriptions.
  foreach (element_children($form['user_cancel_method']) as $element) {
    unset($form['user_cancel_method'][$element]['#description']);
  }

  // Allow to send the account cancellation confirmation mail.
  $form['user_cancel_confirm'] = array(
    '#type' => 'checkbox',
    '#title' => t('Require e-mail confirmation to cancel account.'),
    '#default_value' => FALSE,
    '#description' => t('When enabled, the user must confirm the account cancellation via e-mail.'),
  );
  // Also allow to send account canceled notification mail, if enabled.
  $form['user_cancel_notify'] = array(
    '#type' => 'checkbox',
    '#title' => t('Notify user when account is canceled.'),
    '#default_value' => FALSE,
    '#access' => variable_get('user_mail_status_canceled_notify', FALSE),
    '#description' => t('When enabled, the user will receive an e-mail notification after the account has been cancelled.'),
  );

  return confirm_form($form,
                      t('Are you sure you want to cancel these user accounts?'),
                      'admin/people', t('This action cannot be undone.'),
                      t('Cancel accounts'), t('Cancel'));
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
