# hook_comment_presave()

- **Type:** Hook (documentation function)
- **File:** [`modules/comment/comment.api.php`](_file.md), lines 21–24 · [local source](../../../../source/modules/comment/comment.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.api.php#L21-L24)
- **Module/theme:** comment
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_comment_presave($comment)
```

## Documentation

```text
The comment passed validation and is about to be saved.

Modules may make changes to the comment before it is saved to the database.

@param $comment
  The comment object.
```

## Code

```php
function hook_comment_presave($comment) {
  // Remove leading & trailing spaces from the comment subject.
  $comment->subject = trim($comment->subject);
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_comment_presave()".

- [entity_crud_hook_test_comment_presave()](../../simpletest/tests/entity_crud_hook_test.module/entity_crud_hook_test_comment_presave.md) — `modules/simpletest/tests/entity_crud_hook_test.module`
- [trigger_comment_presave()](../../trigger/trigger.module/trigger_comment_presave.md) — `modules/trigger/trigger.module`

---
_Drupal 7.103 · [modules/comment/comment.api.php](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
