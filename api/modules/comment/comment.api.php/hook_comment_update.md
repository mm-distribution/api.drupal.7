# hook_comment_update()

- **Type:** Hook (documentation function)
- **File:** [`modules/comment/comment.api.php`](_file.md), lines 43–46 · [local source](../../../../source/modules/comment/comment.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.api.php#L43-L46)
- **Module/theme:** comment
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_comment_update($comment)
```

## Documentation

```text
The comment is being updated.

@param $comment
  The comment object.
```

## Code

```php
function hook_comment_update($comment) {
  // Reindex the node when comments are updated.
  search_touch_node($comment->nid);
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_comment_update()".

- [entity_crud_hook_test_comment_update()](../../simpletest/tests/entity_crud_hook_test.module/entity_crud_hook_test_comment_update.md) — `modules/simpletest/tests/entity_crud_hook_test.module`
- [forum_comment_update()](../../forum/forum.module/forum_comment_update.md) — `modules/forum/forum.module`
- [search_comment_update()](../../search/search.module/search_comment_update.md) — `modules/search/search.module`
- [tracker_comment_update()](../../tracker/tracker.module/tracker_comment_update.md) — `modules/tracker/tracker.module`
- [trigger_comment_update()](../../trigger/trigger.module/trigger_comment_update.md) — `modules/trigger/trigger.module`

---
_Drupal 7.103 · [modules/comment/comment.api.php](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
