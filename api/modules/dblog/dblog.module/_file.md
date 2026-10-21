# modules/dblog/dblog.module

- **Source:** [local](../../../../source/modules/dblog/dblog.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.module) · 198 lines
- **Module/theme:** dblog

## File documentation

```text
@file
System monitoring and logging for administrators.

The Database Logging module monitors your site and keeps a list of recorded
events containing usage and performance data, errors, warnings, and similar
operational information.

@see watchdog()
```

## Functions (derived index)

- [dblog_help()](dblog_help.md) — Implements hook_help().
- [dblog_menu()](dblog_menu.md) — Implements hook_menu().
- [dblog_init()](dblog_init.md) — Implements hook_init().
- [dblog_cron()](dblog_cron.md) — Implements hook_cron().
- [_dblog_get_message_types()](_dblog_get_message_types.md) — Gathers a list of uniquely defined database log message types.
- [dblog_watchdog()](dblog_watchdog.md) — Implements hook_watchdog().
- [dblog_form_system_logging_settings_alter()](dblog_form_system_logging_settings_alter.md) — Implements hook_form_FORM_ID_alter() for system_logging_settings().
- [dblog_theme()](dblog_theme.md) — Implements hook_theme().

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
