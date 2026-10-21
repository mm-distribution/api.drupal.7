# user_admin_settings()

- **Type:** Function
- **File:** [`modules/user/user.admin.inc`](_file.md), lines 285–680 · [local source](../../../../source/modules/user/user.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.admin.inc#L285-L680)
- **Module/theme:** user
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function user_admin_settings()
```

## Documentation

```text
Form builder; Configure user settings for this site.

@ingroup forms
@see system_settings_form()
```

## Code

```php
function user_admin_settings() {
  // Settings for anonymous users.
  $form['anonymous_settings'] = array(
    '#type' => 'fieldset',
    '#title' => t('Anonymous users'),
  );
  $form['anonymous_settings']['anonymous'] = array(
    '#type' => 'textfield',
    '#title' => t('Name'),
    '#default_value' => variable_get('anonymous', t('Anonymous')),
    '#description' => t('The name used to indicate anonymous users.'),
    '#required' => TRUE,
  );

  // Administrative role option.
  $form['admin_role'] = array(
    '#type' => 'fieldset',
    '#title' => t('Administrator role'),
  );

  // Do not allow users to set the anonymous or authenticated user roles as the
  // administrator role.
  $roles = user_roles();
  unset($roles[DRUPAL_ANONYMOUS_RID]);
  unset($roles[DRUPAL_AUTHENTICATED_RID]);
  $roles[0] = t('disabled');

  $form['admin_role']['user_admin_role'] = array(
    '#type' => 'select',
    '#title' => t('Administrator role'),
    '#default_value' => variable_get('user_admin_role', 0),
    '#options' => $roles,
    '#description' => t('This role will be automatically assigned new permissions whenever a module is enabled. Changing this setting will not affect existing permissions.'),
  );

  // User registration settings.
  $form['registration_cancellation'] = array(
    '#type' => 'fieldset',
    '#title' => t('Registration and cancellation'),
  );
  $form['registration_cancellation']['user_register'] = array(
    '#type' => 'radios',
    '#title' => t('Who can register accounts?'),
    '#default_value' => variable_get('user_register', USER_REGISTER_VISITORS_ADMINISTRATIVE_APPROVAL),
    '#options' => array(
      USER_REGISTER_ADMINISTRATORS_ONLY => t('Administrators only'),
      USER_REGISTER_VISITORS => t('Visitors'),
      USER_REGISTER_VISITORS_ADMINISTRATIVE_APPROVAL => t('Visitors, but administrator approval is required'),
    )
  );
  $form['registration_cancellation']['user_email_verification'] = array(
    '#type' => 'checkbox',
    '#title' => t('Require e-mail verification when a visitor creates an account.'),
    '#default_value' => variable_get('user_email_verification', TRUE),
    '#description' => t('New users will be required to validate their e-mail address prior to logging into the site, and will be assigned a system-generated password. With this setting disabled, users will be logged in immediately upon registering, and may select their own passwords during registration.')
  );
  module_load_include('inc', 'user', 'user.pages');
  $form['registration_cancellation']['user_cancel_method'] = array(
    '#type' => 'item',
    '#title' => t('When cancelling a user account'),
    '#description' => t('Users with the %select-cancel-method or %administer-users <a href="@permissions-url">permissions</a> can override this default method.', array('%select-cancel-method' => t('Select method for cancelling account'), '%administer-users' => t('Administer users'), '@permissions-url' => url('admin/people/permissions'))),
  );
  $form['registration_cancellation']['user_cancel_method'] += user_cancel_methods();
  foreach (element_children($form['registration_cancellation']['user_cancel_method']) as $element) {
    // Remove all account cancellation methods that have #access defined, as
    // those cannot be configured as default method.
    if (isset($form['registration_cancellation']['user_cancel_method'][$element]['#access'])) {
      $form['registration_cancellation']['user_cancel_method'][$element]['#access'] = FALSE;
    }
    // Remove the description (only displayed on the confirmation form).
    else {
      unset($form['registration_cancellation']['user_cancel_method'][$element]['#description']);
    }
  }

  // Account settings.
  $form['personalization'] = array(
    '#type' => 'fieldset',
    '#title' => t('Personalization'),
  );
  $form['personalization']['user_signatures'] = array(
    '#type' => 'checkbox',
    '#title' => t('Enable signatures.'),
    '#default_value' => variable_get('user_signatures', 0),
  );
  // If picture support is enabled, check whether the picture directory exists.
  if (variable_get('user_pictures', 0)) {
    $picture_path =  file_default_scheme() . '://' . variable_get('user_picture_path', 'pictures');
    if (!file_prepare_directory($picture_path, FILE_CREATE_DIRECTORY)) {
      form_set_error('user_picture_path', t('The directory %directory does not exist or is not writable.', array('%directory' => $picture_path)));
      watchdog('file system', 'The directory %directory does not exist or is not writable.', array('%directory' => $picture_path), WATCHDOG_ERROR);
    }
  }
  $picture_support = variable_get('user_pictures', 0);
  $form['personalization']['user_pictures'] = array(
    '#type' => 'checkbox',
    '#title' => t('Enable user pictures.'),
    '#default_value' => $picture_support,
  );
  drupal_add_js(drupal_get_path('module', 'user') . '/user.js');
  $form['personalization']['pictures'] = array(
    '#type' => 'container',
    '#states' => array(
      // Hide the additional picture settings when user pictures are disabled.
      'invisible' => array(
        'input[name="user_pictures"]' => array('checked' => FALSE),
      ),
    ),
  );
  $form['personalization']['pictures']['user_picture_path'] = array(
    '#type' => 'textfield',
    '#title' => t('Picture directory'),
    '#default_value' => variable_get('user_picture_path', 'pictures'),
    '#size' => 30,
    '#maxlength' => 255,
    '#description' => t('Subdirectory in the file upload directory where pictures will be stored.'),
  );
  $form['personalization']['pictures']['user_picture_default'] = array(
    '#type' => 'textfield',
    '#title' => t('Default picture'),
    '#default_value' => variable_get('user_picture_default', ''),
    '#size' => 30,
    '#maxlength' => 255,
    '#description' => t('URL of picture to display for users with no custom picture selected. Leave blank for none.'),
  );
  if (module_exists('image')) {
    $form['personalization']['pictures']['settings']['user_picture_style'] = array(
      '#type' => 'select',
      '#title' => t('Picture display style'),
      '#options' => image_style_options(TRUE, PASS_THROUGH),
      '#default_value' => variable_get('user_picture_style', ''),
      '#description' => t('The style selected will be used on display, while the original image is retained. Styles may be configured in the <a href="!url">Image styles</a> administration area.', array('!url' => url('admin/config/media/image-styles'))),
    );
  }
  $form['personalization']['pictures']['user_picture_dimensions'] = array(
    '#type' => 'textfield',
    '#title' => t('Picture upload dimensions'),
    '#default_value' => variable_get('user_picture_dimensions', '85x85'),
    '#size' => 10,
    '#maxlength' => 10,
    '#field_suffix' => ' ' . t('pixels'),
    '#description' => t('Pictures larger than this will be scaled down to this size.'),
  );
  $form['personalization']['pictures']['user_picture_file_size'] = array(
    '#type' => 'textfield',
    '#title' => t('Picture upload file size'),
    '#default_value' => variable_get('user_picture_file_size', '30'),
    '#size' => 10,
    '#maxlength' => 10,
    '#field_suffix' => ' ' . t('KB'),
    '#description' => t('Maximum allowed file size for uploaded pictures. Upload size is normally limited only by the PHP maximum post and file upload settings, and images are automatically scaled down to the dimensions specified above.'),
    '#element_validate' => array('element_validate_integer_positive'),
  );
  $form['personalization']['pictures']['user_picture_guidelines'] = array(
    '#type' => 'textarea',
    '#title' => t('Picture guidelines'),
    '#default_value' => variable_get('user_picture_guidelines', ''),
    '#description' => t("This text is displayed at the picture upload form in addition to the default guidelines. It's useful for helping or instructing your users."),
  );

  $form['privacy'] = array(
    '#type' => 'fieldset',
    '#title' => t('Privacy'),
  );
  $form['privacy']['user_password_reset_text'] = array(
    '#type' => 'textarea',
    '#title' => t('Password reset text'),
    '#default_value' => variable_get('user_password_reset_text', t('If %identifier is a valid account, an email will be sent with instructions to reset your password.')),
    '#description' => t('The text that appears when a user successfully submits the password reset form. Due to privacy concerns, it should not contain any information about previously registered users. %identifier will be replaced with what the user entered into the form field.'),
    '#required' => TRUE,
  );

  $form['email_title'] = array(
    '#type' => 'item',
    '#title' => t('E-mails'),
  );
  $form['email'] = array(
    '#type' => 'vertical_tabs',
  );
  // These email tokens are shared for all settings, so just define
  // the list once to help ensure they stay in sync.
  $email_token_help = t('Available variables are: [site:name], [site:url], [user:name], [user:mail], [site:login-url], [site:url-brief], [user:edit-url], [user:one-time-login-url], [user:cancel-url].');

  $form['email_admin_created'] = array(
    '#type' => 'fieldset',
    '#title' => t('Welcome (new user created by administrator)'),
    '#collapsible' => TRUE,
    '#collapsed' => (variable_get('user_register', USER_REGISTER_VISITORS_ADMINISTRATIVE_APPROVAL) != USER_REGISTER_ADMINISTRATORS_ONLY),
    '#description' => t('Edit the welcome e-mail messages sent to new member accounts created by an administrator.') . ' ' . $email_token_help,
    '#group' => 'email',
  );
  $form['email_admin_created']['user_mail_register_admin_created_subject'] = array(
    '#type' => 'textfield',
    '#title' => t('Subject'),
    '#default_value' => _user_mail_text('register_admin_created_subject', NULL, array(), FALSE),
    '#maxlength' => 180,
  );
  $form['email_admin_created']['user_mail_register_admin_created_body'] = array(
    '#type' => 'textarea',
    '#title' => t('Body'),
    '#default_value' => _user_mail_text('register_admin_created_body', NULL, array(), FALSE),
    '#rows' => 15,
  );

  $form['email_pending_approval'] = array(
    '#type' => 'fieldset',
    '#title' => t('Welcome (awaiting approval)'),
    '#collapsible' => TRUE,
    '#collapsed' => (variable_get('user_register', USER_REGISTER_VISITORS_ADMINISTRATIVE_APPROVAL) != USER_REGISTER_VISITORS_ADMINISTRATIVE_APPROVAL),
    '#description' => t('Edit the welcome e-mail messages sent to new members upon registering, when administrative approval is required.') . ' ' . $email_token_help,
    '#group' => 'email',
  );
  $form['email_pending_approval']['user_mail_register_pending_approval_subject'] = array(
    '#type' => 'textfield',
    '#title' => t('Subject'),
    '#default_value' => _user_mail_text('register_pending_approval_subject', NULL, array(), FALSE),
    '#maxlength' => 180,
  );
  $form['email_pending_approval']['user_mail_register_pending_approval_body'] = array(
    '#type' => 'textarea',
    '#title' => t('Body'),
    '#default_value' => _user_mail_text('register_pending_approval_body', NULL, array(), FALSE),
    '#rows' => 8,
  );

  $form['email_no_approval_required'] = array(
    '#type' => 'fieldset',
    '#title' => t('Welcome (no approval required)'),
    '#collapsible' => TRUE,
    '#collapsed' => (variable_get('user_register', USER_REGISTER_VISITORS_ADMINISTRATIVE_APPROVAL) != USER_REGISTER_VISITORS),
    '#description' => t('Edit the welcome e-mail messages sent to new members upon registering, when no administrator approval is required.') . ' ' . $email_token_help,
    '#group' => 'email',
  );
  $form['email_no_approval_required']['user_mail_register_no_approval_required_subject'] = array(
    '#type' => 'textfield',
    '#title' => t('Subject'),
    '#default_value' => _user_mail_text('register_no_approval_required_subject', NULL, array(), FALSE),
    '#maxlength' => 180,
  );
  $form['email_no_approval_required']['user_mail_register_no_approval_required_body'] = array(
    '#type' => 'textarea',
    '#title' => t('Body'),
    '#default_value' => _user_mail_text('register_no_approval_required_body', NULL, array(), FALSE),
    '#rows' => 15,
  );

  $form['email_password_reset'] = array(
    '#type' => 'fieldset',
    '#title' => t('Password recovery'),
    '#collapsible' => TRUE,
    '#collapsed' => TRUE,
    '#description' => t('Edit the e-mail messages sent to users who request a new password.') . ' ' . $email_token_help,
    '#group' => 'email',
    '#weight' => 10,
  );
  $form['email_password_reset']['user_mail_password_reset_subject'] = array(
    '#type' => 'textfield',
    '#title' => t('Subject'),
    '#default_value' => _user_mail_text('password_reset_subject', NULL, array(), FALSE),
    '#maxlength' => 180,
  );
  $form['email_password_reset']['user_mail_password_reset_body'] = array(
    '#type' => 'textarea',
    '#title' => t('Body'),
    '#default_value' => _user_mail_text('password_reset_body', NULL, array(), FALSE),
    '#rows' => 12,
  );

  $form['email_activated'] = array(
    '#type' => 'fieldset',
    '#title' => t('Account activation'),
    '#collapsible' => TRUE,
    '#collapsed' => TRUE,
    '#description' => t('Enable and edit e-mail messages sent to users upon account activation (when an administrator activates an account of a user who has already registered, on a site where administrative approval is required).') . ' ' . $email_token_help,
    '#group' => 'email',
  );
  $form['email_activated']['user_mail_status_activated_notify'] = array(
    '#type' => 'checkbox',
    '#title' => t('Notify user when account is activated.'),
    '#default_value' => variable_get('user_mail_status_activated_notify', TRUE),
  );
  $form['email_activated']['settings'] = array(
    '#type' => 'container',
    '#states' => array(
      // Hide the additional settings when this email is disabled.
      'invisible' => array(
        'input[name="user_mail_status_activated_notify"]' => array('checked' => FALSE),
      ),
    ),
  );
  $form['email_activated']['settings']['user_mail_status_activated_subject'] = array(
    '#type' => 'textfield',
    '#title' => t('Subject'),
    '#default_value' => _user_mail_text('status_activated_subject', NULL, array(), FALSE),
    '#maxlength' => 180,
  );
  $form['email_activated']['settings']['user_mail_status_activated_body'] = array(
    '#type' => 'textarea',
    '#title' => t('Body'),
    '#default_value' => _user_mail_text('status_activated_body', NULL, array(), FALSE),
    '#rows' => 15,
  );

  $form['email_blocked'] = array(
    '#type' => 'fieldset',
    '#title' => t('Account blocked'),
    '#collapsible' => TRUE,
    '#collapsed' => TRUE,
    '#description' => t('Enable and edit e-mail messages sent to users when their accounts are blocked.') . ' ' . $email_token_help,
    '#group' => 'email',
  );
  $form['email_blocked']['user_mail_status_blocked_notify'] = array(
    '#type' => 'checkbox',
    '#title' => t('Notify user when account is blocked.'),
    '#default_value' => variable_get('user_mail_status_blocked_notify', FALSE),
  );
  $form['email_blocked']['settings'] = array(
    '#type' => 'container',
    '#states' => array(
      // Hide the additional settings when the blocked email is disabled.
      'invisible' => array(
        'input[name="user_mail_status_blocked_notify"]' => array('checked' => FALSE),
      ),
    ),
  );
  $form['email_blocked']['settings']['user_mail_status_blocked_subject'] = array(
    '#type' => 'textfield',
    '#title' => t('Subject'),
    '#default_value' => _user_mail_text('status_blocked_subject', NULL, array(), FALSE),
    '#maxlength' => 180,
  );
  $form['email_blocked']['settings']['user_mail_status_blocked_body'] = array(
    '#type' => 'textarea',
    '#title' => t('Body'),
    '#default_value' => _user_mail_text('status_blocked_body', NULL, array(), FALSE),
    '#rows' => 3,
  );

  $form['email_cancel_confirm'] = array(
    '#type' => 'fieldset',
    '#title' => t('Account cancellation confirmation'),
    '#collapsible' => TRUE,
    '#collapsed' => TRUE,
    '#description' => t('Edit the e-mail messages sent to users when they attempt to cancel their accounts.') . ' ' . $email_token_help,
    '#group' => 'email',
  );
  $form['email_cancel_confirm']['user_mail_cancel_confirm_subject'] = array(
    '#type' => 'textfield',
    '#title' => t('Subject'),
    '#default_value' => _user_mail_text('cancel_confirm_subject', NULL, array(), FALSE),
    '#maxlength' => 180,
  );
  $form['email_cancel_confirm']['user_mail_cancel_confirm_body'] = array(
    '#type' => 'textarea',
    '#title' => t('Body'),
    '#default_value' => _user_mail_text('cancel_confirm_body', NULL, array(), FALSE),
    '#rows' => 3,
  );

  $form['email_canceled'] = array(
    '#type' => 'fieldset',
    '#title' => t('Account canceled'),
    '#collapsible' => TRUE,
    '#collapsed' => TRUE,
    '#description' => t('Enable and edit e-mail messages sent to users when their accounts are canceled.') . ' ' . $email_token_help,
    '#group' => 'email',
  );
  $form['email_canceled']['user_mail_status_canceled_notify'] = array(
    '#type' => 'checkbox',
    '#title' => t('Notify user when account is canceled.'),
    '#default_value' => variable_get('user_mail_status_canceled_notify', FALSE),
  );
  $form['email_canceled']['settings'] = array(
    '#type' => 'container',
    '#states' => array(
      // Hide the settings when the cancel notify checkbox is disabled.
      'invisible' => array(
        'input[name="user_mail_status_canceled_notify"]' => array('checked' => FALSE),
      ),
    ),
  );
  $form['email_canceled']['settings']['user_mail_status_canceled_subject'] = array(
    '#type' => 'textfield',
    '#title' => t('Subject'),
    '#default_value' => _user_mail_text('status_canceled_subject', NULL, array(), FALSE),
    '#maxlength' => 180,
  );
  $form['email_canceled']['settings']['user_mail_status_canceled_body'] = array(
    '#type' => 'textarea',
    '#title' => t('Body'),
    '#default_value' => _user_mail_text('status_canceled_body', NULL, array(), FALSE),
    '#rows' => 3,
  );

  return system_settings_form($form);
}
```

---
_Drupal 7.103 · [modules/user/user.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/user/user.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
