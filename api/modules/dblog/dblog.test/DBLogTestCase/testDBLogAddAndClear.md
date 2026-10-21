# DBLogTestCase::testDBLogAddAndClear()

- **Type:** Method
- **File:** [`modules/dblog/dblog.test`](../_file.md), lines 469–497 · [local source](../../../../../source/modules/dblog/dblog.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test#L469-L497)
- **Class:** [DBLogTestCase](../DBLogTestCase.md)
- **Module/theme:** dblog

## Signature

```php
protected function testDBLogAddAndClear()
```

## Documentation

```text
Tests the addition and clearing of log events through the admin interface.

Logs in the admin user, creates a database log event, and tests the
functionality of clearing the database log through the admin interface.
```

## Code

```php
  protected function testDBLogAddAndClear() {
    global $base_root;
    // Get a count of how many watchdog entries already exist.
    $count = db_query('SELECT COUNT(*) FROM {watchdog}')->fetchField();
    $log = array(
      'type'        => 'custom',
      'message'     => 'Log entry added to test the doClearTest clear down.',
      'variables'   => array(),
      'severity'    => WATCHDOG_NOTICE,
      'link'        => NULL,
      'user'        => $this->big_user,
      'uid'         => isset($this->big_user->uid) ? $this->big_user->uid : 0,
      'request_uri' => $base_root . request_uri(),
      'referer'     => $_SERVER['HTTP_REFERER'],
      'ip'          => ip_address(),
      'timestamp'   => REQUEST_TIME,
    );
    // Add a watchdog entry.
    dblog_watchdog($log);
    // Make sure the table count has actually been incremented.
    $this->assertEqual($count + 1, db_query('SELECT COUNT(*) FROM {watchdog}')->fetchField(), format_string('dblog_watchdog() added an entry to the dblog :count', array(':count' => $count)));
    // Login the admin user.
    $this->drupalLogin($this->big_user);
    // Post in order to clear the database table.
    $this->drupalPost('admin/reports/dblog', array(), t('Clear log messages'));
    // Count the rows in watchdog that previously related to the deleted user.
    $count = db_query('SELECT COUNT(*) FROM {watchdog}')->fetchField();
    $this->assertEqual($count, 0, format_string('DBLog contains :count records after a clear.', array(':count' => $count)));
  }
```

---
_Drupal 7.103 · [modules/dblog/dblog.test](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test) · Licensed GPL-2.0-or-later (see LICENSE)._
