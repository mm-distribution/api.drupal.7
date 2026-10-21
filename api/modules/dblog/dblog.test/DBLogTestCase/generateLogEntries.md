# DBLogTestCase::generateLogEntries()

- **Type:** Method
- **File:** [`modules/dblog/dblog.test`](../_file.md), lines 167–194 · [local source](../../../../../source/modules/dblog/dblog.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test#L167-L194)
- **Class:** [DBLogTestCase](../DBLogTestCase.md)
- **Module/theme:** dblog

## Signature

```php
private function generateLogEntries($count, $type = 'custom', $severity = WATCHDOG_NOTICE)
```

## Documentation

```text
Generates a number of random database log events.

@param int $count
  Number of watchdog entries to generate.
@param string $type
  (optional) The type of watchdog entry. Defaults to 'custom'.
@param int $severity
  (optional) The severity of the watchdog entry. Defaults to WATCHDOG_NOTICE.
```

## Code

```php
  private function generateLogEntries($count, $type = 'custom', $severity = WATCHDOG_NOTICE) {
    global $base_root;

    // This long URL makes it just a little bit harder to pass the link part of
    // the test with a mix of English words and a repeating series of random
    // percent-encoded Chinese characters.
    $link = urldecode('/content/xo%E9%85%B1%E5%87%89%E6%8B%8C%E7%B4%A0%E9%B8%A1%E7%85%A7%E7%83%A7%E9%B8%A1%E9%BB%84%E7%8E%AB%E7%91%B0-%E7%A7%91%E5%B7%9E%E7%9A%84%E5%B0%8F%E4%B9%9D%E5%AF%A8%E6%B2%9F%E7%BB%9D%E7%BE%8E%E9%AB%98%E5%B1%B1%E6%B9%96%E6%B3%8A%E9%85%B1%E5%87%89%E6%8B%8C%E7%B4%A0%E9%B8%A1%E7%85%A7%E7%83%A7%E9%B8%A1%E9%BB%84%E7%8E%AB%E7%91%B0-%E7%A7%91%E5%B7%9E%E7%9A%84%E5%B0%8F%E4%B9%9D%E5%AF%A8%E6%B2%9F%E7%BB%9D%E7%BE%8E%E9%AB%98%E5%B1%B1%E6%B9%96%E6%B3%8A%E9%85%B1%E5%87%89%E6%8B%8C%E7%B4%A0%E9%B8%A1%E7%85%A7%E7%83%A7%E9%B8%A1%E9%BB%84%E7%8E%AB%E7%91%B0-%E7%A7%91%E5%B7%9E%E7%9A%84%E5%B0%8F%E4%B9%9D%E5%AF%A8%E6%B2%9F%E7%BB%9D%E7%BE%8E%E9%AB%98%E5%B1%B1%E6%B9%96%E6%B3%8A%E9%85%B1%E5%87%89%E6%8B%8C%E7%B4%A0%E9%B8%A1%E7%85%A7%E7%83%A7%E9%B8%A1%E9%BB%84%E7%8E%AB%E7%91%B0-%E7%A7%91%E5%B7%9E%E7%9A%84%E5%B0%8F%E4%B9%9D%E5%AF%A8%E6%B2%9F%E7%BB%9D%E7%BE%8E%E9%AB%98%E5%B1%B1%E6%B9%96%E6%B3%8A%E9%85%B1%E5%87%89%E6%8B%8C%E7%B4%A0%E9%B8%A1%E7%85%A7%E7%83%A7%E9%B8%A1%E9%BB%84%E7%8E%AB%E7%91%B0-%E7%A7%91%E5%B7%9E%E7%9A%84%E5%B0%8F%E4%B9%9D%E5%AF%A8%E6%B2%9F%E7%BB%9D%E7%BE%8E%E9%AB%98%E5%B1%B1%E6%B9%96%E6%B3%8A%E9%85%B1%E5%87%89%E6%8B%8C%E7%B4%A0%E9%B8%A1%E7%85%A7%E7%83%A7%E9%B8%A1%E9%BB%84%E7%8E%AB%E7%91%B0-%E7%A7%91%E5%B7%9E%E7%9A%84%E5%B0%8F%E4%B9%9D%E5%AF%A8%E6%B2%9F%E7%BB%9D%E7%BE%8E%E9%AB%98%E5%B1%B1%E6%B9%96%E6%B3%8A%E9%85%B1%E5%87%89%E6%8B%8C%E7%B4%A0%E9%B8%A1%E7%85%A7%E7%83%A7%E9%B8%A1%E9%BB%84%E7%8E%AB%E7%91%B0-%E7%A7%91%E5%B7%9E%E7%9A%84%E5%B0%8F%E4%B9%9D%E5%AF%A8%E6%B2%9F%E7%BB%9D%E7%BE%8E%E9%AB%98%E5%B1%B1%E6%B9%96%E6%B3%8A%E9%85%B1%E5%87%89%E6%8B%8C%E7%B4%A0%E9%B8%A1%E7%85%A7%E7%83%A7%E9%B8%A1%E9%BB%84%E7%8E%AB%E7%91%B0-%E7%A7%91%E5%B7%9E%E7%9A%84%E5%B0%8F%E4%B9%9D%E5%AF%A8%E6%B2%9F%E7%BB%9D%E7%BE%8E%E9%AB%98%E5%B1%B1%E6%B9%96%E6%B3%8A%E9%85%B1%E5%87%89%E6%8B%8C%E7%B4%A0%E9%B8%A1%E7%85%A7%E7%83%A7%E9%B8%A1%E9%BB%84%E7%8E%AB%E7%91%B0-%E7%A7%91%E5%B7%9E%E7%9A%84%E5%B0%8F%E4%B9%9D%E5%AF%A8%E6%B2%9F%E7%BB%9D%E7%BE%8E%E9%AB%98%E5%B1%B1%E6%B9%96%E6%B3%8A%E9%85%B1%E5%87%89%E6%8B%8C%E7%B4%A0%E9%B8%A1%E7%85%A7%E7%83%A7%E9%B8%A1%E9%BB%84%E7%8E%AB%E7%91%B0-%E7%A7%91%E5%B7%9E%E7%9A%84%E5%B0%8F%E4%B9%9D%E5%AF%A8%E6%B2%9F%E7%BB%9D%E7%BE%8E%E9%AB%98%E5%B1%B1%E6%B9%96%E6%B3%8A%E9%85%B1%E5%87%89%E6%8B%8C%E7%B4%A0%E9%B8%A1%E7%85%A7%E7%83%A7%E9%B8%A1%E9%BB%84%E7%8E%AB%E7%91%B0-%E7%A7%91%E5%B7%9E%E7%9A%84%E5%B0%8F%E4%B9%9D%E5%AF%A8%E6%B2%9F%E7%BB%9D%E7%BE%8E%E9%AB%98%E5%B1%B1%E6%B9%96%E6%B3%8A%E9%85%B1%E5%87%89%E6%8B%8C%E7%B4%A0%E9%B8%A1%E7%85%A7%E7%83%A7%E9%B8%A1%E9%BB%84%E7%8E%AB%E7%91%B0-%E7%A7%91%E5%B7%9E%E7%9A%84%E5%B0%8F%E4%B9%9D%E5%AF%A8%E6%B2%9F%E7%BB%9D%E7%BE%8E%E9%AB%98%E5%B1%B1%E6%B9%96%E6%B3%8A%E9%85%B1%E5%87%89%E6%8B%8C%E7%B4%A0%E9%B8%A1%E7%85%A7%E7%83%A7%E9%B8%A1%E9%BB%84%E7%8E%AB%E7%91%B0-%E7%A7%91%E5%B7%9E%E7%9A%84%E5%B0%8F%E4%B9%9D%E5%AF%A8%E6%B2%9F%E7%BB%9D%E7%BE%8E%E9%AB%98%E5%B1%B1%E6%B9%96%E6%B3%8A-lake-isabelle');

    // Prepare the fields to be logged
    $log = array(
      'type'        => $type,
      'message'     => 'Log entry added to test the dblog row limit.',
      'variables'   => array(),
      'severity'    => $severity,
      'link'        => $link,
      'user'        => $this->big_user,
      'uid'         => isset($this->big_user->uid) ? $this->big_user->uid : 0,
      'request_uri' => $base_root . request_uri(),
      'referer'     => $_SERVER['HTTP_REFERER'],
      'ip'          => ip_address(),
      'timestamp'   => REQUEST_TIME,
      );
    $message = 'Log entry added to test the dblog row limit. Entry #';
    for ($i = 0; $i < $count; $i++) {
      $log['message'] = $message . $i;
      dblog_watchdog($log);
    }
  }
```

---
_Drupal 7.103 · [modules/dblog/dblog.test](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test) · Licensed GPL-2.0-or-later (see LICENSE)._
