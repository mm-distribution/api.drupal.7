# syslog_form_system_logging_settings_alter()

- **Type:** Function
- **File:** [`modules/syslog/syslog.module`](_file.md), lines 47–71 · [local source](../../../../source/modules/syslog/syslog.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/syslog/syslog.module#L47-L71)
- **Module/theme:** syslog
- **Implements:** [hook_form_FORM_ID_alter()](../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function syslog_form_system_logging_settings_alter(&$form, &$form_state)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter().
```

## Code

```php
function syslog_form_system_logging_settings_alter(&$form, &$form_state) {
  $help = module_exists('help') ? ' ' . l(t('More information'), 'admin/help/syslog') . '.' : NULL;
  $form['syslog_identity'] = array(
    '#type'          => 'textfield',
    '#title'         => t('Syslog identity'),
    '#default_value' => variable_get('syslog_identity', 'drupal'),
    '#description'   => t('A string that will be prepended to every message logged to Syslog. If you have multiple sites logging to the same Syslog log file, a unique identity per site makes it easy to tell the log entries apart.') . $help,
  );
  if (defined('LOG_LOCAL0')) {
    $form['syslog_facility'] = array(
      '#type'          => 'select',
      '#title'         => t('Syslog facility'),
      '#default_value' => variable_get('syslog_facility', LOG_LOCAL0),
      '#options'       => syslog_facility_list(),
      '#description'   => t('Depending on the system configuration, Syslog and other logging tools use this code to identify or filter messages from within the entire system log.') . $help,
     );
  }
  $form['syslog_format'] = array(
    '#type'          => 'textarea',
    '#title'         => t('Syslog format'),
    '#default_value' => variable_get('syslog_format', '!base_url|!timestamp|!type|!ip|!request_uri|!referer|!uid|!link|!message'),
    '#description'   => t('Specify the format of the syslog entry. Available variables are: <dl><dt><code>!base_url</code></dt><dd>Base URL of the site.</dd><dt><code>!timestamp</code></dt><dd>Unix timestamp of the log entry.</dd><dt><code>!type</code></dt><dd>The category to which this message belongs.</dd><dt><code>!ip</code></dt><dd>IP address of the user triggering the message.</dd><dt><code>!request_uri</code></dt><dd>The requested URI.</dd><dt><code>!referer</code></dt><dd>HTTP Referer if available.</dd><dt><code>!uid</code></dt><dd>User ID.</dd><dt><code>!link</code></dt><dd>A link to associate with the message.</dd><dt><code>!message</code></dt><dd>The message to store in the log.</dd></dl>'),
  );
  $form['actions']['#weight'] = 1;
}
```

---
_Drupal 7.103 · [modules/syslog/syslog.module](https://github.com/drupal/drupal/blob/7.103/modules/syslog/syslog.module) · Licensed GPL-2.0-or-later (see LICENSE)._
