# CommentActionsTestCase

- **Type:** Class
- **File:** [`modules/comment/comment.test`](_file.md), lines 1953–2104 · [local source](../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L1953-L2104)
- **Module/theme:** comment

## Signature

```php
class CommentActionsTestCase extends CommentHelperCase
```

## Documentation

```text
Test actions provided by the comment module.
```

## Methods (derived index)

- [getInfo()](CommentActionsTestCase/getInfo.md)
- [testCommentPublishUnpublishActions()](CommentActionsTestCase/testCommentPublishUnpublishActions.md) — Test comment publish and unpublish actions.
- [testCommentUnpublishByKeyword()](CommentActionsTestCase/testCommentUnpublishByKeyword.md) — Tests the unpublish comment by keyword action.
- [testCommentPublishUnpublishHooks()](CommentActionsTestCase/testCommentPublishUnpublishHooks.md) — Test comment publish and unpublish hooks.
- [assertWatchdogMessage()](CommentActionsTestCase/assertWatchdogMessage.md) — Verify that a watchdog message has been entered.
- [clearWatchdog()](CommentActionsTestCase/clearWatchdog.md) — Helper function: clear the watchdog.
- [assertHookMessage()](CommentActionsTestCase/assertHookMessage.md) — Pass if the message $text was set by one of the comment hooks in comment_hook_test.module, i.e., if the $text is an element of $_SESSION['comment_hook_test'].

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
