# syslog_watchdog()

- **Type:** Function
- **File:** [`modules/syslog/syslog.module`](_file.md), lines 95–119 · [local source](../../../../source/modules/syslog/syslog.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/syslog/syslog.module#L95-L119)
- **Module/theme:** syslog
- **Implements:** [hook_watchdog()](../../system/system.api.php/hook_watchdog.md)

## Signature

```php
function syslog_watchdog(array $log_entry)
```

## Documentation

```text
Implements hook_watchdog().
```

## Code

```php
function syslog_watchdog(array $log_entry) {
  global $base_url;

  $log_init = &drupal_static(__FUNCTION__, FALSE);

  if (!$log_init) {
    $log_init = TRUE;
    $default_facility = defined('LOG_LOCAL0') ? LOG_LOCAL0 : LOG_USER;
    openlog(variable_get('syslog_identity', 'drupal'), LOG_NDELAY, variable_get('syslog_facility', $default_facility));
  }

  $message = strtr(variable_get('syslog_format', '!base_url|!timestamp|!type|!ip|!request_uri|!referer|!uid|!link|!message'), array(
    '!base_url'    => $base_url,
    '!timestamp'   => $log_entry['timestamp'],
    '!type'        => $log_entry['type'],
    '!ip'          => $log_entry['ip'],
    '!request_uri' => $log_entry['request_uri'],
    '!referer'     => $log_entry['referer'],
    '!uid'         => $log_entry['uid'],
    '!link'        => strip_tags((string) $log_entry['link']),
    '!message'     => strip_tags((string) (!isset($log_entry['variables']) ? $log_entry['message'] : strtr($log_entry['message'], $log_entry['variables']))),
  ));

  syslog($log_entry['severity'], $message);
}
```

---
_Drupal 7.103 · [modules/syslog/syslog.module](https://github.com/drupal/drupal/blob/7.103/modules/syslog/syslog.module) · Licensed GPL-2.0-or-later (see LICENSE)._
