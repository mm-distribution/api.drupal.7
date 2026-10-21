# hook_comment_insert()

- **Type:** Hook (documentation function)
- **File:** [`modules/comment/comment.api.php`](_file.md), lines 32–35 · [local source](../../../../source/modules/comment/comment.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.api.php#L32-L35)
- **Module/theme:** comment
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_comment_insert($comment)
```

## Documentation

```text
The comment is being inserted.

@param $comment
  The comment object.
```

## Code

```php
function hook_comment_insert($comment) {
  // Reindex the node when comments are added.
  search_touch_node($comment->nid);
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_comment_insert()".

- [entity_crud_hook_test_comment_insert()](../../simpletest/tests/entity_crud_hook_test.module/entity_crud_hook_test_comment_insert.md) — `modules/simpletest/tests/entity_crud_hook_test.module`
- [search_comment_insert()](../../search/search.module/search_comment_insert.md) — `modules/search/search.module`
- [trigger_comment_insert()](../../trigger/trigger.module/trigger_comment_insert.md) — `modules/trigger/trigger.module`

---
_Drupal 7.103 · [modules/comment/comment.api.php](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
