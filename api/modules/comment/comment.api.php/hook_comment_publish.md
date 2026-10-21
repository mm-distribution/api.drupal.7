# hook_comment_publish()

- **Type:** Hook (documentation function)
- **File:** [`modules/comment/comment.api.php`](_file.md), lines 115–117 · [local source](../../../../source/modules/comment/comment.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.api.php#L115-L117)
- **Module/theme:** comment
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_comment_publish($comment)
```

## Documentation

```text
Act on a comment that is being saved in a published state.

@param $comment
  Passes in the comment the action is being performed on.
@return
  Nothing.
```

## Code

```php
function hook_comment_publish($comment) {
  drupal_set_message(t('Comment: @subject has been published', array('@subject' => $comment->subject)));
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_comment_publish()".

- [comment_hook_test_comment_publish()](../tests/comment_hook_test.module/comment_hook_test_comment_publish.md) — `modules/comment/tests/comment_hook_test.module`
- [forum_comment_publish()](../../forum/forum.module/forum_comment_publish.md) — `modules/forum/forum.module`
- [search_comment_publish()](../../search/search.module/search_comment_publish.md) — `modules/search/search.module`
- [tracker_comment_publish()](../../tracker/tracker.module/tracker_comment_publish.md) — `modules/tracker/tracker.module`

---
_Drupal 7.103 · [modules/comment/comment.api.php](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
