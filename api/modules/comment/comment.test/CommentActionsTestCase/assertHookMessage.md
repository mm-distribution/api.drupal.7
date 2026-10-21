# CommentActionsTestCase::assertHookMessage()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 2098–2103 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L2098-L2103)
- **Class:** [CommentActionsTestCase](../CommentActionsTestCase.md)
- **Module/theme:** comment

## Signature

```php
protected function assertHookMessage($text, $message = NULL, $group = 'Other')
```

## Documentation

```text
Pass if the message $text was set by one of the comment hooks in
comment_hook_test.module, i.e., if the $text is an element of
$_SESSION['comment_hook_test'].

@param $text
  Plain text to look for.
@param $message
  Message to display.
@param $group
  The group this message belongs to, defaults to 'Other'.
@return
  TRUE on pass, FALSE on fail.
```

## Code

```php
  protected function assertHookMessage($text, $message = NULL, $group = 'Other') {
    if (!isset($message)) {
      $message = $text;
    }
    return $this->assertTrue(array_search($text, $_SESSION['comment_hook_test']) !== FALSE, $message, $group);
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
