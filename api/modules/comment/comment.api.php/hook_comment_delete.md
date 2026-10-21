# hook_comment_delete()

- **Type:** Hook (documentation function)
- **File:** [`modules/comment/comment.api.php`](_file.md), lines 139–141 · [local source](../../../../source/modules/comment/comment.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.api.php#L139-L141)
- **Module/theme:** comment
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_comment_delete($comment)
```

## Documentation

```text
The comment is being deleted by the moderator.

@param $comment
  Passes in the comment the action is being performed on.
@return
  Nothing.
```

## Code

```php
function hook_comment_delete($comment) {
  drupal_set_message(t('Comment: @subject has been deleted', array('@subject' => $comment->subject)));
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_comment_delete()".

- [entity_crud_hook_test_comment_delete()](../../simpletest/tests/entity_crud_hook_test.module/entity_crud_hook_test_comment_delete.md) — `modules/simpletest/tests/entity_crud_hook_test.module`
- [forum_comment_delete()](../../forum/forum.module/forum_comment_delete.md) — `modules/forum/forum.module`
- [search_comment_delete()](../../search/search.module/search_comment_delete.md) — `modules/search/search.module`
- [tracker_comment_delete()](../../tracker/tracker.module/tracker_comment_delete.md) — `modules/tracker/tracker.module`
- [trigger_comment_delete()](../../trigger/trigger.module/trigger_comment_delete.md) — `modules/trigger/trigger.module`

---
_Drupal 7.103 · [modules/comment/comment.api.php](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
