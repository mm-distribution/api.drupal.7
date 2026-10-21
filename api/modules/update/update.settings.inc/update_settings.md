# update_settings()

- **Type:** Function
- **File:** [`modules/update/update.settings.inc`](_file.md), lines 15–61 · [local source](../../../../source/modules/update/update.settings.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.settings.inc#L15-L61)
- **Module/theme:** update
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function update_settings($form)
```

## Documentation

```text
Form constructor for the update settings form.

@see update_settings_validate()
@see update_settings_submit()
@ingroup forms
```

## Code

```php
function update_settings($form) {
  $form['update_check_frequency'] = array(
    '#type' => 'radios',
    '#title' => t('Check for updates'),
    '#default_value' => variable_get('update_check_frequency', 1),
    '#options' => array(
      '1' => t('Daily'),
      '7' => t('Weekly'),
    ),
    '#description' => t('Select how frequently you want to automatically check for new releases of your currently installed modules and themes.'),
  );

  $form['update_check_disabled'] = array(
    '#type' => 'checkbox',
    '#title' => t('Check for updates of disabled and uninstalled modules and themes'),
    '#default_value' => variable_get('update_check_disabled', FALSE),
  );

  $notify_emails = variable_get('update_notify_emails', array());
  $form['update_notify_emails'] = array(
    '#type' => 'textarea',
    '#title' => t('E-mail addresses to notify when updates are available'),
    '#rows' => 4,
    '#default_value' => implode("\n", $notify_emails),
    '#description' => t('Whenever your site checks for available updates and finds new releases, it can notify a list of users via e-mail. Put each address on a separate line. If blank, no e-mails will be sent.'),
  );

  $form['update_notification_threshold'] = array(
    '#type' => 'radios',
    '#title' => t('E-mail notification threshold'),
    '#default_value' => variable_get('update_notification_threshold', 'all'),
    '#options' => array(
      'all' => t('All newer versions'),
      'security' => t('Only security updates'),
    ),
    '#description' => t('You can choose to send e-mail only if a security update is available, or to be notified about all newer versions. If there are updates available of Drupal core or any of your installed modules and themes, your site will always print a message on the <a href="@status_report">status report</a> page, and will also display an error message on administration pages if there is a security update.', array('@status_report' => url('admin/reports/status')))
  );

  $form = system_settings_form($form);
  // Custom validation callback for the email notification setting.
  $form['#validate'][] = 'update_settings_validate';
  // We need to call our own submit callback first, not the one from
  // system_settings_form(), so that we can process and save the emails.
  unset($form['#submit']);

  return $form;
}
```

---
_Drupal 7.103 · [modules/update/update.settings.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.settings.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
