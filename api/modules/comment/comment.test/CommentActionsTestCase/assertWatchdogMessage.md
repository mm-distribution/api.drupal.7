# CommentActionsTestCase::assertWatchdogMessage()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 2072–2075 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L2072-L2075)
- **Class:** [CommentActionsTestCase](../CommentActionsTestCase.md)
- **Module/theme:** comment

## Signature

```php
function assertWatchdogMessage($watchdog_message, $variables, $message)
```

## Documentation

```text
Verify that a watchdog message has been entered.

@param $watchdog_message
  The watchdog message.
@param $variables
  The array of variables passed to watchdog().
@param $message
  The assertion message.
```

## Code

```php
  function assertWatchdogMessage($watchdog_message, $variables, $message) {
    $status = (bool) db_query_range("SELECT 1 FROM {watchdog} WHERE message = :message AND variables = :variables", 0, 1, array(':message' => $watchdog_message, ':variables' => serialize($variables)))->fetchField();
    return $this->assert($status, format_string('@message', array('@message' => $message)));
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
