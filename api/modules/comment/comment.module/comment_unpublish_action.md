# comment_unpublish_action()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 2605–2619 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L2605-L2619)
- **Module/theme:** comment
- **Topics:** [actions](../../../topics/actions.md)

## Signature

```php
function comment_unpublish_action($comment, $context = array())
```

## Documentation

```text
Unpublishes a comment.

@param $comment
  An optional comment object.
@param array $context
  Array with components:
  - 'cid': Comment ID. Required if $comment is not given.

@ingroup actions
```

## Code

```php
function comment_unpublish_action($comment, $context = array()) {
  if (isset($comment->subject)) {
    $subject = $comment->subject;
    $comment->status = COMMENT_NOT_PUBLISHED;
  }
  else {
    $cid = $context['cid'];
    $subject = db_query('SELECT subject FROM {comment} WHERE cid = :cid', array(':cid' => $cid))->fetchField();
    db_update('comment')
      ->fields(array('status' => COMMENT_NOT_PUBLISHED))
      ->condition('cid', $cid)
      ->execute();
  }
  watchdog('action', 'Unpublished comment %subject.', array('%subject' => $subject));
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
