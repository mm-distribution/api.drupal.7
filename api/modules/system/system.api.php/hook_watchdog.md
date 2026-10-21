# hook_watchdog()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 2522–2570 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L2522-L2570)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_watchdog(array $log_entry)
```

## Documentation

```text
Log an event message.

This hook allows modules to route log events to custom destinations, such as
SMS, Email, pager, syslog, ...etc.

@param $log_entry
  An associative array containing the following keys:
  - type: The type of message for this entry.
  - user: The user object for the user who was logged in when the event
    happened.
  - uid: The user ID for the user who was logged in when the event happened.
  - request_uri: The request URI for the page the event happened in.
  - referer: The page that referred the user to the page where the event
    occurred.
  - ip: The IP address where the request for the page came from.
  - timestamp: The UNIX timestamp of the date/time the event occurred.
  - severity: The severity of the message; one of the following values as
    defined in @link http://www.faqs.org/rfcs/rfc3164.html RFC 3164: @endlink
    - WATCHDOG_EMERGENCY: Emergency, system is unusable.
    - WATCHDOG_ALERT: Alert, action must be taken immediately.
    - WATCHDOG_CRITICAL: Critical conditions.
    - WATCHDOG_ERROR: Error conditions.
    - WATCHDOG_WARNING: Warning conditions.
    - WATCHDOG_NOTICE: Normal but significant conditions.
    - WATCHDOG_INFO: Informational messages.
    - WATCHDOG_DEBUG: Debug-level messages.
  - link: An optional link provided by the module that called the watchdog()
    function.
  - message: The text of the message to be logged. Variables in the message
    are indicated by using placeholder strings alongside the variables
    argument to declare the value of the placeholders. See t() for
    documentation on how the message and variable parameters interact.
  - variables: An array of variables to be inserted into the message on
    display. Will be NULL or missing if a message is already translated or if
    the message is not possible to translate.
```

## Code

```php
function hook_watchdog(array $log_entry) {
  global $base_url, $language;

  $severity_list = array(
    WATCHDOG_EMERGENCY => t('Emergency'),
    WATCHDOG_ALERT     => t('Alert'),
    WATCHDOG_CRITICAL  => t('Critical'),
    WATCHDOG_ERROR     => t('Error'),
    WATCHDOG_WARNING   => t('Warning'),
    WATCHDOG_NOTICE    => t('Notice'),
    WATCHDOG_INFO      => t('Info'),
    WATCHDOG_DEBUG     => t('Debug'),
  );

  $to = 'someone@example.com';
  $params = array();
  $params['subject'] = t('[@site_name] @severity_desc: Alert from your web site', array(
    '@site_name' => variable_get('site_name', 'Drupal'),
    '@severity_desc' => $severity_list[$log_entry['severity']],
  ));

  $params['message']  = "\nSite:         @base_url";
  $params['message'] .= "\nSeverity:     (@severity) @severity_desc";
  $params['message'] .= "\nTimestamp:    @timestamp";
  $params['message'] .= "\nType:         @type";
  $params['message'] .= "\nIP Address:   @ip";
  $params['message'] .= "\nRequest URI:  @request_uri";
  $params['message'] .= "\nReferrer URI: @referer_uri";
  $params['message'] .= "\nUser:         (@uid) @name";
  $params['message'] .= "\nLink:         @link";
  $params['message'] .= "\nMessage:      \n\n@message";

  $params['message'] = t($params['message'], array(
    '@base_url'      => $base_url,
    '@severity'      => $log_entry['severity'],
    '@severity_desc' => $severity_list[$log_entry['severity']],
    '@timestamp'     => format_date($log_entry['timestamp']),
    '@type'          => $log_entry['type'],
    '@ip'            => $log_entry['ip'],
    '@request_uri'   => $log_entry['request_uri'],
    '@referer_uri'   => $log_entry['referer'],
    '@uid'           => $log_entry['uid'],
    '@name'          => $log_entry['user']->name,
    '@link'          => strip_tags($log_entry['link']),
    '@message'       => strip_tags($log_entry['message']),
  ));

  drupal_mail('emaillog', 'entry', $to, $language, $params);
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_watchdog()".

- [actions_loop_test_watchdog()](../../simpletest/tests/actions_loop_test.module/actions_loop_test_watchdog.md) — `modules/simpletest/tests/actions_loop_test.module`
- [entity_cache_test_watchdog()](../../simpletest/tests/entity_cache_test.module/entity_cache_test_watchdog.md) — `modules/simpletest/tests/entity_cache_test.module`
- [system_test_watchdog()](../../simpletest/tests/system_test.module/system_test_watchdog.md) — `modules/simpletest/tests/system_test.module`
- [dblog_watchdog()](../../dblog/dblog.module/dblog_watchdog.md) — `modules/dblog/dblog.module`
- [syslog_watchdog()](../../syslog/syslog.module/syslog_watchdog.md) — `modules/syslog/syslog.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
