# Logging severity levels

- **Topic id:** `logging_severity_levels`
- **Defined in:** [`includes/bootstrap.inc`](../includes/bootstrap.inc/_file.md), line 55 · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L55)

## Documentation

```text
@defgroup logging_severity_levels Logging severity levels
@{
Logging severity levels as defined in RFC 3164.

The WATCHDOG_* constant definitions correspond to the logging severity levels
defined in RFC 3164, section 4.1.1. PHP supplies predefined LOG_* constants
for use in the syslog() function, but their values on Windows builds do not
correspond to RFC 3164. The associated PHP bug report was closed with the
comment, "And it's also not a bug, as Windows just have less log levels,"
and "So the behavior you're seeing is perfectly normal."

@see http://www.faqs.org/rfcs/rfc3164.html
@see http://bugs.php.net/bug.php?id=18090
@see http://php.net/manual/function.syslog.php
@see http://php.net/manual/network.constants.php
@see watchdog()
@see watchdog_severity_levels()
```

## Members (derived, 12)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [dblog_overview()](../modules/dblog/dblog.admin.inc/dblog_overview.md) (function) — Page callback: Displays a listing of database log messages.
- [drupal_error_levels()](../includes/errors.inc/drupal_error_levels.md) (function) — Maps PHP error constants to watchdog severity levels.
- [watchdog_severity_levels()](../includes/common.inc/watchdog_severity_levels.md) (function) — Returns a list of severity levels, as defined in RFC 3164.
- [WATCHDOG_ALERT](../includes/bootstrap.inc/_file.md#watchdog_alert) (constant) — Log message severity -- Alert: action must be taken immediately.
- [WATCHDOG_CRITICAL](../includes/bootstrap.inc/_file.md#watchdog_critical) (constant) — Log message severity -- Critical conditions.
- [WATCHDOG_DEBUG](../includes/bootstrap.inc/_file.md#watchdog_debug) (constant) — Log message severity -- Debug-level messages.
- [WATCHDOG_EMERGENCY](../includes/bootstrap.inc/_file.md#watchdog_emergency) (constant) — Log message severity -- Emergency: system is unusable.
- [WATCHDOG_ERROR](../includes/bootstrap.inc/_file.md#watchdog_error) (constant) — Log message severity -- Error conditions.
- [WATCHDOG_INFO](../includes/bootstrap.inc/_file.md#watchdog_info) (constant) — Log message severity -- Informational messages.
- [WATCHDOG_NOTICE](../includes/bootstrap.inc/_file.md#watchdog_notice) (constant) — Log message severity -- Normal but significant conditions.
- [WATCHDOG_WARNING](../includes/bootstrap.inc/_file.md#watchdog_warning) (constant) — Log message severity -- Warning conditions.
- [DBLogTestCase::getSeverityConstant()](../modules/dblog/dblog.test/DBLogTestCase/getSeverityConstant.md) (method) — Gets the watchdog severity constant corresponding to the CSS class.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
