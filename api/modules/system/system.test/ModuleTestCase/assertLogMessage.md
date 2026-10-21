# ModuleTestCase::assertLogMessage()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 115–126 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L115-L126)
- **Class:** [ModuleTestCase](../ModuleTestCase.md)
- **Module/theme:** system

## Signature

```php
function assertLogMessage($type, $message, $variables = array(), $severity = WATCHDOG_NOTICE, $link = '')
```

## Documentation

```text
Verify a log entry was entered for a module's status change.
Called in the same way of the expected original watchdog() execution.

@param $type
  The category to which this message belongs.
@param $message
  The message to store in the log. Keep $message translatable
  by not concatenating dynamic values into it! Variables in the
  message should be added by using placeholder strings alongside
  the variables argument to declare the value of the placeholders.
  See t() for documentation on how $message and $variables interact.
@param $variables
  Array of variables to replace in the message on display or
  NULL if message is already translated or not possible to
  translate.
@param $severity
  The severity of the message, as per RFC 3164.
@param $link
  A link to associate with the message.
```

## Code

```php
  function assertLogMessage($type, $message, $variables = array(), $severity = WATCHDOG_NOTICE, $link = '') {
    $count = db_select('watchdog', 'w')
      ->condition('type', $type)
      ->condition('message', $message)
      ->condition('variables', serialize($variables))
      ->condition('severity', $severity)
      ->condition('link', $link)
      ->countQuery()
      ->execute()
      ->fetchField();
    $this->assertTrue($count > 0, format_string('watchdog table contains @count rows for @message', array('@count' => $count, '@message' => $message)));
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
