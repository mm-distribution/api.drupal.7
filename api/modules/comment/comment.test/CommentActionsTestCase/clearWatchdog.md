# CommentActionsTestCase::clearWatchdog()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 2080–2082 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L2080-L2082)
- **Class:** [CommentActionsTestCase](../CommentActionsTestCase.md)
- **Module/theme:** comment

## Signature

```php
function clearWatchdog()
```

## Documentation

```text
Helper function: clear the watchdog.
```

## Code

```php
  function clearWatchdog() {
    db_truncate('watchdog')->execute();
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
