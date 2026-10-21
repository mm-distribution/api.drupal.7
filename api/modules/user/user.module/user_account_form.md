# user_account_form()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 1054–1230 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L1054-L1230)
- **Module/theme:** user

## Signature

```php
function user_account_form(&$form, &$form_state)
```

## Documentation

```text
Helper function to add default user account fields to user registration and edit form.

@see user_account_form_validate()
@see user_validate_current_pass()
@see user_validate_picture()
@see user_validate_mail()
```

## Code

```php
function user_account_form(&$form, &$form_state) {
  global $user;

  $account = $form['#user'];
  $register = ($form['#user']->uid > 0 ? FALSE : TRUE);

  $admin = user_access('administer users');

  $form['#validate'][] = 'user_account_form_validate';

  // Account information.
  $form['account'] = array(
    '#type'   => 'container',
    '#weight' => -10,
  );
  // Only show name field on registration form or user can change own username.
  $form['account']['name'] = array(
    '#type' => 'textfield',
    '#title' => t('Username'),
    '#maxlength' => USERNAME_MAX_LENGTH,
    '#description' => t('Spaces are allowed; punctuation is not allowed except for periods, hyphens, apostrophes, and underscores.'),
    '#required' => TRUE,
    '#attributes' => array('class' => array('username')),
    '#default_value' => (!$register ? $account->name : ''),
    '#access' => ($register || ($user->uid == $account->uid && user_access('change own username')) || $admin),
    '#weight' => -10,
  );

  $form['account']['mail'] = array(
    '#type' => 'textfield',
    '#title' => t('E-mail address'),
    '#maxlength' => EMAIL_MAX_LENGTH,
    '#description' => t('A valid e-mail address. All e-mails from the system will be sent to this address. The e-mail address is not made public and will only be used if you wish to receive a new password or wish to receive certain news or notifications by e-mail.'),
    '#required' => TRUE,
    '#default_value' => (!$register ? $account->mail : ''),
  );

  // Display password field only for existing users or when user is allowed to
  // assign a password during registration.
  if (!$register) {
    $form['account']['pass'] = array(
      '#type' => 'password_confirm',
      '#size' => 25,
      '#description' => t('To change the current user password, enter the new password in both fields.'),
    );
    // To skip the current password field, the user must have logged in via a
    // one-time link and have the token in the URL. Store this in $form_state
    // so it persists even on subsequent Ajax requests.
    if (!isset($form_state['user_pass_reset'])) {
      $form_state['user_pass_reset'] = isset($_SESSION['pass_reset_' . $account->uid]) && isset($_GET['pass-reset-token']) && ($_GET['pass-reset-token'] == $_SESSION['pass_reset_' . $account->uid]);
    }
    $protected_values = array();
    $current_pass_description = '';
    // The user may only change their own password without their current
    // password if they logged in via a one-time login link.
    if (!$form_state['user_pass_reset']) {
      $protected_values['mail'] = $form['account']['mail']['#title'];
      $protected_values['pass'] = t('Password');
      $request_new = l(t('Request new password'), 'user/password', array('attributes' => array('title' => t('Request new password via e-mail.'))));
      $current_pass_description = t('Enter your current password to change the %mail or %pass. !request_new.', array('%mail' => $protected_values['mail'], '%pass' => $protected_values['pass'], '!request_new' => $request_new));
    }
    // The user must enter their current password to change to a new one.
    if ($user->uid == $account->uid) {
      $form['account']['current_pass_required_values'] = array(
        '#type' => 'value',
        '#value' => $protected_values,
      );
      $form['account']['current_pass'] = array(
        '#type' => 'password',
        '#title' => t('Current password'),
        '#size' => 25,
        '#access' => !empty($protected_values),
        '#description' => $current_pass_description,
        '#weight' => -5,
        // Do not let web browsers remember this password, since we are trying
        // to confirm that the person submitting the form actually knows the
        // current one.
        '#attributes' => array('autocomplete' => 'off'),
      );
      $form['#validate'][] = 'user_validate_current_pass';
    }
  }
  elseif (!variable_get('user_email_verification', TRUE) || $admin) {
    $form['account']['pass'] = array(
      '#type' => 'password_confirm',
      '#size' => 25,
      '#description' => t('Provide a password for the new account in both fields.'),
      '#required' => TRUE,
    );
  }

  if ($admin) {
    $status = isset($account->status) ? $account->status : 1;
  }
  else {
    $status = $register ? variable_get('user_register', USER_REGISTER_VISITORS_ADMINISTRATIVE_APPROVAL) == USER_REGISTER_VISITORS : $account->status;
  }
  $form['account']['status'] = array(
    '#type' => 'radios',
    '#title' => t('Status'),
    '#default_value' => $status,
    '#options' => array(t('Blocked'), t('Active')),
    '#access' => $admin,
  );

  $roles = array_map('check_plain', user_roles(TRUE));
  // The disabled checkbox subelement for the 'authenticated user' role
  // must be generated separately and added to the checkboxes element,
  // because of a limitation in Form API not supporting a single disabled
  // checkbox within a set of checkboxes.
  // @todo This should be solved more elegantly. See issue #119038.
  $checkbox_authenticated = array(
    '#type' => 'checkbox',
    '#title' => $roles[DRUPAL_AUTHENTICATED_RID],
    '#default_value' => TRUE,
    '#disabled' => TRUE,
  );
  unset($roles[DRUPAL_AUTHENTICATED_RID]);
  $form['account']['roles'] = array(
    '#type' => 'checkboxes',
    '#title' => t('Roles'),
    '#default_value' => (!$register && !empty($account->roles) ? array_keys(array_filter($account->roles)) : array()),
    '#options' => $roles,
    '#access' => $roles && user_access('administer permissions'),
    DRUPAL_AUTHENTICATED_RID => $checkbox_authenticated,
  );

  $form['account']['notify'] = array(
    '#type' => 'checkbox',
    '#title' => t('Notify user of new account'),
    '#access' => $register && $admin,
  );

  // Signature.
  $form['signature_settings'] = array(
    '#type' => 'fieldset',
    '#title' => t('Signature settings'),
    '#weight' => 1,
    '#access' => (!$register && variable_get('user_signatures', 0)),
  );

  $form['signature_settings']['signature'] = array(
    '#type' => 'text_format',
    '#title' => t('Signature'),
    '#default_value' => isset($account->signature) ? $account->signature : '',
    '#description' => t('Your signature will be publicly displayed at the end of your comments.'),
    '#format' => isset($account->signature_format) ? $account->signature_format : NULL,
  );

  // Picture/avatar.
  $form['picture'] = array(
    '#type' => 'fieldset',
    '#title' => t('Picture'),
    '#weight' => 1,
    '#access' => (!$register && variable_get('user_pictures', 0)),
  );
  $form['picture']['picture'] = array(
    '#type' => 'value',
    '#value' => isset($account->picture) ? $account->picture : NULL,
  );
  $form['picture']['picture_current'] = array(
    '#markup' => theme('user_picture', array('account' => $account)),
  );
  $form['picture']['picture_delete'] = array(
    '#type' => 'checkbox',
    '#title' => t('Delete picture'),
    '#access' => !empty($account->picture->fid),
    '#description' => t('Check this box to delete your current picture.'),
  );
  $form['picture']['picture_upload'] = array(
    '#type' => 'file',
    '#title' => t('Upload picture'),
    '#size' => 48,
    '#description' => t('Your virtual face or picture. Pictures larger than @dimensions pixels will be scaled down.', array('@dimensions' => variable_get('user_picture_dimensions', '85x85'))) . ' ' . filter_xss_admin(variable_get('user_picture_guidelines', '')),
  );
  $form['#validate'][] = 'user_validate_picture';
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
