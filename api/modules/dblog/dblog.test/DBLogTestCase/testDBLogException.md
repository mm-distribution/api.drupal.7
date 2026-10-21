# DBLogTestCase::testDBLogException()

- **Type:** Method
- **File:** [`modules/dblog/dblog.test`](../_file.md), lines 574–596 · [local source](../../../../../source/modules/dblog/dblog.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test#L574-L596)
- **Class:** [DBLogTestCase](../DBLogTestCase.md)
- **Module/theme:** dblog

## Signature

```php
protected function testDBLogException()
```

## Documentation

```text
Verifies that exceptions are caught in dblog_watchdog().
```

## Code

```php
  protected function testDBLogException() {
    $log = array(
      'type'        => 'custom',
      'message'     => 'Log entry added to test watchdog handling of Exceptions.',
      'variables'   => array(),
      'severity'    => WATCHDOG_NOTICE,
      'link'        => NULL,
      'user'        => $this->big_user,
      'uid'         => isset($this->big_user->uid) ? $this->big_user->uid : 0,
      'request_uri' => request_uri(),
      'referer'     => $_SERVER['HTTP_REFERER'],
      'ip'          => ip_address(),
      'timestamp'   => REQUEST_TIME,
    );

    // Remove watchdog table temporarily to simulate it missing during
    // installation.
    db_query("DROP TABLE {watchdog}");

    // Add a watchdog entry.
    // This should not throw an Exception, but fail silently.
    dblog_watchdog($log);
  }
```

---
_Drupal 7.103 · [modules/dblog/dblog.test](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test) · Licensed GPL-2.0-or-later (see LICENSE)._
