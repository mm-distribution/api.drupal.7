# modules/syslog/syslog.module

- **Source:** [local](../../../../source/modules/syslog/syslog.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/syslog/syslog.module) · 120 lines
- **Module/theme:** syslog

## File documentation

```text
@file
Redirects logging messages to syslog.
```

## Functions (derived index)

- [syslog_help()](syslog_help.md) — Implements hook_help().
- [syslog_form_system_logging_settings_alter()](syslog_form_system_logging_settings_alter.md) — Implements hook_form_FORM_ID_alter().
- [syslog_facility_list()](syslog_facility_list.md) — Lists all possible syslog facilities for UNIX/Linux.
- [syslog_watchdog()](syslog_watchdog.md) — Implements hook_watchdog().

## Constants

### DEFAULT_SYSLOG_FACILITY

- Line 18

```php
define('DEFAULT_SYSLOG_FACILITY', LOG_LOCAL0);
```

```text
Sets the proper logging facility.

Note that LOG_LOCAL0 through LOG_LOCAL7 are not available on Windows, so we
check for availability. If LOG_LOCAL0 is defined by the PHP environment, we
set that as the default; if not, we use LOG_USER.

@see http://php.net/manual/function.syslog.php
```

### DEFAULT_SYSLOG_FACILITY

- Line 21

```php
define('DEFAULT_SYSLOG_FACILITY', LOG_USER);
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
