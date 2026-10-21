# _update_cron_notify()

- **Type:** Function
- **File:** [`modules/update/update.fetch.inc`](_file.md), lines 347–379 · [local source](../../../../source/modules/update/update.fetch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.fetch.inc#L347-L379)
- **Module/theme:** update

## Signature

```php
function _update_cron_notify()
```

## Documentation

```text
Performs any notifications that should be done once cron fetches new data.

This method checks the status of the site using the new data and, depending
on the configuration of the site, notifies administrators via e-mail if there
are new releases or missing security updates.

@see update_requirements()
```

## Code

```php
function _update_cron_notify() {
  module_load_install('update');
  $status = update_requirements('runtime');
  $params = array();
  $notify_all = (variable_get('update_notification_threshold', 'all') == 'all');
  foreach (array('core', 'contrib') as $report_type) {
    $type = 'update_' . $report_type;
    if (isset($status[$type]['severity'])
        && ($status[$type]['severity'] == REQUIREMENT_ERROR || ($notify_all && $status[$type]['reason'] == UPDATE_NOT_CURRENT))) {
      $params[$report_type] = $status[$type]['reason'];
    }
  }
  if (!empty($params)) {
    $notify_list = variable_get('update_notify_emails', '');
    if (!empty($notify_list)) {
      $default_language = language_default();
      foreach ($notify_list as $target) {
        if ($target_user = user_load_by_mail($target)) {
          $target_language = user_preferred_language($target_user);
        }
        else {
          $target_language = $default_language;
        }
        $message = drupal_mail('update', 'status_notify', $target, $target_language, $params);
        // Track when the last mail was successfully sent to avoid sending
        // too many e-mails.
        if ($message['result']) {
          variable_set('update_last_email_notification', REQUEST_TIME);
        }
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/update/update.fetch.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.fetch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
