# update_mail()

- **Type:** Function
- **File:** [`modules/update/update.module`](_file.md), lines 525–543 · [local source](../../../../source/modules/update/update.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module#L525-L543)
- **Module/theme:** update
- **Implements:** [hook_mail()](../../system/system.api.php/hook_mail.md)

## Signature

```php
function update_mail($key, &$message, $params)
```

## Documentation

```text
Implements hook_mail().

Constructs the e-mail notification message when the site is out of date.

@param $key
  Unique key to indicate what message to build, always 'status_notify'.
@param $message
  Reference to the message array being built.
@param $params
  Array of parameters to indicate what kind of text to include in the message
  body. This is a keyed array of message type ('core' or 'contrib') as the
  keys, and the status reason constant (UPDATE_NOT_SECURE, etc) for the
  values.

@see drupal_mail()
@see _update_cron_notify()
@see _update_message_text()
```

## Code

```php
function update_mail($key, &$message, $params) {
  $language = $message['language'];
  $langcode = $language->language;
  $message['subject'] .= t('New release(s) available for !site_name', array('!site_name' => variable_get('site_name', 'Drupal')), array('langcode' => $langcode));
  foreach ($params as $msg_type => $msg_reason) {
    $message['body'][] = _update_message_text($msg_type, $msg_reason, FALSE, $language);
  }
  $message['body'][] = t('See the available updates page for more information:', array(), array('langcode' => $langcode)) . "\n" . url('admin/reports/updates', array('absolute' => TRUE, 'language' => $language));
  if (update_manager_access()) {
    $message['body'][] = t('You can automatically install your missing updates using the Update manager:', array(), array('langcode' => $langcode)) . "\n" . url('admin/reports/updates/update', array('absolute' => TRUE, 'language' => $language));
  }
  $settings_url = url('admin/reports/updates/settings', array('absolute' => TRUE));
  if (variable_get('update_notification_threshold', 'all') == 'all') {
    $message['body'][] = t('Your site is currently configured to send these emails when any updates are available. To get notified only for security updates, !url.', array('!url' => $settings_url));
  }
  else {
    $message['body'][] = t('Your site is currently configured to send these emails only when security updates are available. To get notified for any available updates, !url.', array('!url' => $settings_url));
  }
}
```

---
_Drupal 7.103 · [modules/update/update.module](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module) · Licensed GPL-2.0-or-later (see LICENSE)._
