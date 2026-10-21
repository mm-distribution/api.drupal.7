# DBLogTestCase

- **Type:** Class
- **File:** [`modules/dblog/dblog.test`](_file.md), lines 11–744 · [local source](../../../../source/modules/dblog/dblog.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test#L11-L744)
- **Module/theme:** dblog

## Signature

```php
class DBLogTestCase extends DrupalWebTestCase
```

## Documentation

```text
Tests logging messages to the database.
```

## Properties

### $big_user

```php
protected $big_user;
```

```text
A user with some relevant administrative permissions.

@var object
```

### $any_user

```php
protected $any_user;
```

```text
A user without any permissions.

@var object
```

## Methods (derived index)

- [getInfo()](DBLogTestCase/getInfo.md)
- [setUp()](DBLogTestCase/setUp.md) — Enable modules and create users with specific permissions.
- [testDBLog()](DBLogTestCase/testDBLog.md) — Tests Database Logging module functionality through interfaces.
- [testDBLogCorrupted()](DBLogTestCase/testDBLogCorrupted.md) — Tests corrupted log entries can still display available data.
- [verifyRowLimit()](DBLogTestCase/verifyRowLimit.md) — Verifies setting of the database log row limit.
- [verifyCron()](DBLogTestCase/verifyCron.md) — Verifies that cron correctly applies the database log row limit.
- [generateLogEntries()](DBLogTestCase/generateLogEntries.md) — Generates a number of random database log events.
- [verifyReports()](DBLogTestCase/verifyReports.md) — Confirms that database log reports are displayed at the correct paths.
- [verifyEvents()](DBLogTestCase/verifyEvents.md) — Generates and then verifies various types of events.
- [doUser()](DBLogTestCase/doUser.md) — Generates and then verifies some user events.
- [doNode()](DBLogTestCase/doNode.md) — Generates and then verifies some node events.
- [getContent()](DBLogTestCase/getContent.md) — Creates random content based on node content type.
- [getContentUpdate()](DBLogTestCase/getContentUpdate.md) — Creates random content as an update based on node content type.
- [testDBLogAddAndClear()](DBLogTestCase/testDBLogAddAndClear.md) — Tests the addition and clearing of log events through the admin interface.
- [testFilter()](DBLogTestCase/testFilter.md) — Tests the database log filter functionality at admin/reports/dblog.
- [testDBLogException()](DBLogTestCase/testDBLogException.md) — Verifies that exceptions are caught in dblog_watchdog().
- [getLogEntries()](DBLogTestCase/getLogEntries.md) — Gets the database log event information from the browser page.
- [getTypeCount()](DBLogTestCase/getTypeCount.md) — Gets the count of database log entries by database log event type.
- [getSeverityConstant()](DBLogTestCase/getSeverityConstant.md) — Gets the watchdog severity constant corresponding to the CSS class.
- [asText()](DBLogTestCase/asText.md) — Extracts the text contained by the XHTML element.
- [assertLogMessage()](DBLogTestCase/assertLogMessage.md) — Confirms that a log message appears on the database log overview screen.
- [testLogMessageSanitized()](DBLogTestCase/testLogMessageSanitized.md) — Make sure HTML tags are filtered out in the log detail page.

---
_Drupal 7.103 · [modules/dblog/dblog.test](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test) · Licensed GPL-2.0-or-later (see LICENSE)._
