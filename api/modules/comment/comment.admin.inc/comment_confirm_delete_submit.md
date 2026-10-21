# comment_confirm_delete_submit()

- **Type:** Function
- **File:** [`modules/comment/comment.admin.inc`](_file.md), lines 274–284 · [local source](../../../../source/modules/comment/comment.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.admin.inc#L274-L284)
- **Module/theme:** comment

## Signature

```php
function comment_confirm_delete_submit($form, &$form_state)
```

## Documentation

```text
Process comment_confirm_delete form submissions.
```

## Code

```php
function comment_confirm_delete_submit($form, &$form_state) {
  $comment = $form['#comment'];
  // Delete the comment and its replies.
  comment_delete($comment->cid);
  drupal_set_message(t('The comment and all its replies have been deleted.'));
  watchdog('content', 'Deleted comment @cid and its replies.', array('@cid' => $comment->cid));
  // Clear the cache so an anonymous user sees that his comment was deleted.
  cache_clear_all();

  $form_state['redirect'] = "node/$comment->nid";
}
```

---
_Drupal 7.103 · [modules/comment/comment.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
