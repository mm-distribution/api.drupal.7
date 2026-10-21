# comment_unpublish_by_keyword_action()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 2635–2647 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L2635-L2647)
- **Module/theme:** comment
- **Topics:** [actions](../../../topics/actions.md)

## Signature

```php
function comment_unpublish_by_keyword_action($comment, $context)
```

## Documentation

```text
Unpublishes a comment if it contains certain keywords.

@param object $comment
  Comment object to modify.
@param array $context
  Array with components:
  - 'keywords': Keywords to look for. If the comment contains at least one
    of the keywords, it is unpublished.

@ingroup actions
@see comment_unpublish_by_keyword_action_form()
@see comment_unpublish_by_keyword_action_submit()
```

## Code

```php
function comment_unpublish_by_keyword_action($comment, $context) {
  $node = node_load($comment->nid);
  $build = comment_view($comment, $node);
  $text = drupal_render($build);
  foreach ($context['keywords'] as $keyword) {
    if (strpos($text, $keyword) !== FALSE) {
      $comment->status = COMMENT_NOT_PUBLISHED;
      comment_save($comment);
      watchdog('action', 'Unpublished comment %subject.', array('%subject' => $comment->subject));
      break;
    }
  }
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
