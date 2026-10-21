# DBLogTestCase::testLogMessageSanitized()

- **Type:** Method
- **File:** [`modules/dblog/dblog.test`](../_file.md), lines 720–743 · [local source](../../../../../source/modules/dblog/dblog.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test#L720-L743)
- **Class:** [DBLogTestCase](../DBLogTestCase.md)
- **Module/theme:** dblog

## Signature

```php
public function testLogMessageSanitized()
```

## Documentation

```text
Make sure HTML tags are filtered out in the log detail page.
```

## Code

```php
  public function testLogMessageSanitized() {
    $this->drupalLogin($this->big_user);

    // Make sure dangerous HTML tags are filtered out in log detail page.
    $log = array(
      'uid' => 0,
      'type' => 'custom',
      'message' => "<script>alert('foo');</script> <strong>Lorem ipsum</strong>",
      'variables' => NULL,
      'severity' => WATCHDOG_NOTICE,
      'link' => 'foo/bar',
      'request_uri' => 'http://example.com?dblog=1',
      'referer' => 'http://example.org?dblog=2',
      'ip' => '0.0.1.0',
      'timestamp' => REQUEST_TIME,
    );
    dblog_watchdog($log);

    $wid = db_query('SELECT MAX(wid) FROM {watchdog}')->fetchField();
    $this->drupalGet('admin/reports/event/' . $wid);
    $this->assertResponse(200);
    $this->assertNoRaw("<script>alert('foo');</script>");
    $this->assertRaw("alert('foo'); <strong>Lorem ipsum</strong>");
  }
```

---
_Drupal 7.103 · [modules/dblog/dblog.test](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test) · Licensed GPL-2.0-or-later (see LICENSE)._
