# hook_comment_view()

- **Type:** Hook (documentation function)
- **File:** [`modules/comment/comment.api.php`](_file.md), lines 73–76 · [local source](../../../../source/modules/comment/comment.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.api.php#L73-L76)
- **Module/theme:** comment
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_comment_view($comment, $view_mode, $langcode)
```

## Documentation

```text
The comment is being viewed. This hook can be used to add additional data to the comment before theming.

@param $comment
  Passes in the comment the action is being performed on.
@param $view_mode
  View mode, e.g. 'full', 'teaser'...
@param $langcode
  The language code used for rendering.

@see hook_entity_view()
```

## Code

```php
function hook_comment_view($comment, $view_mode, $langcode) {
  // how old is the comment
  $comment->time_ago = time() - $comment->changed;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_comment_view()".

- [trigger_comment_view()](../../trigger/trigger.module/trigger_comment_view.md) — `modules/trigger/trigger.module`
- [user_comment_view()](../../user/user.module/user_comment_view.md) — `modules/user/user.module`

---
_Drupal 7.103 · [modules/comment/comment.api.php](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
