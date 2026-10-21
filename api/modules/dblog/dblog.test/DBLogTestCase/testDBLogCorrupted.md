# DBLogTestCase::testDBLogCorrupted()

- **Type:** Method
- **File:** [`modules/dblog/dblog.test`](../_file.md), lines 71–95 · [local source](../../../../../source/modules/dblog/dblog.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test#L71-L95)
- **Class:** [DBLogTestCase](../DBLogTestCase.md)
- **Module/theme:** dblog

## Signature

```php
private function testDBLogCorrupted()
```

## Documentation

```text
Tests corrupted log entries can still display available data.
```

## Code

```php
  private function testDBLogCorrupted() {
    global $base_root;

    // Prepare the fields to be logged
    $log = array(
      'type'        => 'custom',
      'message'     => 'Log entry added to test the unserialize failure.',
      'variables'   => 'BAD SERIALIZED DATA',
      'severity'    => WATCHDOG_NOTICE,
      'link'        => '',
      'user'        => $this->big_user,
      'uid'         => isset($this->big_user->uid) ? $this->big_user->uid : 0,
      'request_uri' => $base_root . request_uri(),
      'referer'     => $_SERVER['HTTP_REFERER'],
      'ip'          => ip_address(),
      'timestamp'   => REQUEST_TIME,
    );
    dblog_watchdog($log);

    // View the database log report page.
    $this->drupalGet('admin/reports/dblog');
    $this->assertResponse(200);
    $output = truncate_utf8(filter_xss(t('Log data is corrupted and cannot be unserialized: Log entry added to test unserialize failure.'), array()), 56, TRUE, TRUE);
    $this->assertText($output, 'Log data is corrupted and cannot be unserialized.');
  }
```

---
_Drupal 7.103 · [modules/dblog/dblog.test](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test) · Licensed GPL-2.0-or-later (see LICENSE)._
