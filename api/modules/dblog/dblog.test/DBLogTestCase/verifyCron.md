# DBLogTestCase::verifyCron()

- **Type:** Method
- **File:** [`modules/dblog/dblog.test`](../_file.md), lines 124–155 · [local source](../../../../../source/modules/dblog/dblog.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test#L124-L155)
- **Class:** [DBLogTestCase](../DBLogTestCase.md)
- **Module/theme:** dblog

## Signature

```php
private function verifyCron($row_limit)
```

## Documentation

```text
Verifies that cron correctly applies the database log row limit.

@param int $row_limit
  The row limit.
```

## Code

```php
  private function verifyCron($row_limit) {
    // Generate additional log entries.
    $this->generateLogEntries($row_limit + 10);
    // Verify that the database log row count exceeds the row limit.
    $count = db_query('SELECT COUNT(wid) FROM {watchdog}')->fetchField();
    $this->assertTrue($count > $row_limit, format_string('Dblog row count of @count exceeds row limit of @limit', array('@count' => $count, '@limit' => $row_limit)));

    // Get last ID to compare against; log entries get deleted, so we can't
    // reliably add the number of newly created log entries to the current count
    // to measure number of log entries created by cron.
    $last_id = db_query('SELECT MAX(wid) FROM {watchdog}')->fetchField();

    // Run a cron job.
    $this->cronRun();

    // Get last ID after cron was run.
    $current_id = db_query('SELECT MAX(wid) FROM {watchdog}')->fetchField();

    // Only one final "cron is finished" message should be logged.
    $this->assertEqual($current_id - $last_id, 1, format_string('Cron added @count of @expected new log entries', array('@count' => $current_id - $last_id, '@expected' => 1)));

    // Test enabling of detailed cron logging.
    // Get the number of enabled modules. Cron adds a log entry for each module.
    $module_count = count(module_implements('cron'));
    variable_set('cron_detailed_logging', 1);
    $last_id = db_query('SELECT MAX(wid) FROM {watchdog}')->fetchField();
    $this->cronRun();
    $current_id = db_query('SELECT MAX(wid) FROM {watchdog}')->fetchField();

    // The number of log entries created.
    $this->assertEqual($current_id - $last_id, $module_count + 2, format_string('Cron added @count of @expected new log entries', array('@count' => $current_id - $last_id, '@expected' => $module_count + 2)));
  }
```

---
_Drupal 7.103 · [modules/dblog/dblog.test](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test) · Licensed GPL-2.0-or-later (see LICENSE)._
