# DBLogTestCase::assertLogMessage()

- **Type:** Method
- **File:** [`modules/dblog/dblog.test`](../_file.md), lines 709–715 · [local source](../../../../../source/modules/dblog/dblog.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test#L709-L715)
- **Class:** [DBLogTestCase](../DBLogTestCase.md)
- **Module/theme:** dblog

## Signature

```php
protected function assertLogMessage($log_message, $message)
```

## Documentation

```text
Confirms that a log message appears on the database log overview screen.

This function should only be used for the admin/reports/dblog page, because
it checks for the message link text truncated to 56 characters. Other log
pages have no detail links so they contain the full message text.

@param string $log_message
  The database log message to check.
@param string $message
  The message to pass to simpletest.
```

## Code

```php
  protected function assertLogMessage($log_message, $message) {
    $message_text = truncate_utf8(filter_xss($log_message, array()), 56, TRUE, TRUE);
    // After filter_xss(), HTML entities should be converted to their character
    // equivalents because assertLink() uses this string in xpath() to query the
    // Document Object Model (DOM).
    $this->assertLink(html_entity_decode($message_text), 0, $message);
  }
```

---
_Drupal 7.103 · [modules/dblog/dblog.test](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test) · Licensed GPL-2.0-or-later (see LICENSE)._
