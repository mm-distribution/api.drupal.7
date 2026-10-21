# dblog_watchdog()

- **Type:** Function
- **File:** [`modules/dblog/dblog.module`](_file.md), lines 146–171 · [local source](../../../../source/modules/dblog/dblog.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.module#L146-L171)
- **Module/theme:** dblog
- **Implements:** [hook_watchdog()](../../system/system.api.php/hook_watchdog.md)

## Signature

```php
function dblog_watchdog(array $log_entry)
```

## Documentation

```text
Implements hook_watchdog().

Note: Some values may be truncated to meet database column size restrictions.
```

## Code

```php
function dblog_watchdog(array $log_entry) {
  if (!function_exists('drupal_substr')) {
    require_once DRUPAL_ROOT . '/includes/unicode.inc';
  }
  try {
    Database::getConnection('default', 'default')->insert('watchdog')
      ->fields(array(
        'uid' => $log_entry['uid'],
        'type' => drupal_substr($log_entry['type'], 0, 64),
        'message' => $log_entry['message'],
        'variables' => serialize($log_entry['variables']),
        'severity' => $log_entry['severity'],
        'link' => drupal_substr($log_entry['link'], 0, 255),
        'location' => $log_entry['request_uri'],
        'referer' => $log_entry['referer'],
        'hostname' => drupal_substr($log_entry['ip'], 0, 128),
        'timestamp' => $log_entry['timestamp'],
      ))
      ->execute();
  }
  catch (Exception $e) {
    // Exception is ignored so that watchdog does not break pages during the
    // installation process or is not able to create the watchdog table during
    // installation.
  }
}
```

---
_Drupal 7.103 · [modules/dblog/dblog.module](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.module) · Licensed GPL-2.0-or-later (see LICENSE)._
