# comment_form_submit()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 2253–2296 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L2253-L2296)
- **Module/theme:** comment

## Signature

```php
function comment_form_submit($form, &$form_state)
```

## Documentation

```text
Process comment form submissions; prepare the comment, store it, and set a redirection target.
```

## Code

```php
function comment_form_submit($form, &$form_state) {
  $node = node_load($form_state['values']['nid']);
  $comment = comment_form_submit_build_comment($form, $form_state);
  if (user_access('post comments') && (user_access('administer comments') || $node->comment == COMMENT_NODE_OPEN)) {
    // Save the anonymous user information to a cookie for reuse.
    if (user_is_anonymous()) {
      user_cookie_save(array_intersect_key($form_state['values'], array_flip(array('name', 'mail', 'homepage'))));
    }

    comment_save($comment);
    $form_state['values']['cid'] = $comment->cid;

    // Add an entry to the watchdog log.
    watchdog('content', 'Comment posted: %subject.', array('%subject' => $comment->subject), WATCHDOG_NOTICE, l(t('view'), 'comment/' . $comment->cid, array('fragment' => 'comment-' . $comment->cid)));

    // Explain the approval queue if necessary.
    if ($comment->status == COMMENT_NOT_PUBLISHED) {
      if (!user_access('administer comments')) {
        drupal_set_message(t('Your comment has been queued for review by site administrators and will be published after approval.'));
      }
    }
    else {
      drupal_set_message(t('Your comment has been posted.'));
    }
    $query = array();
    // Find the current display page for this comment.
    $page = comment_get_display_page($comment->cid, $node->type);
    if ($page > 0) {
      $query['page'] = $page;
    }
    // Redirect to the newly posted comment.
    $redirect = array('node/' . $node->nid, array('query' => $query, 'fragment' => 'comment-' . $comment->cid));
  }
  else {
    watchdog('content', 'Comment: unauthorized comment submitted or comment submitted to a closed post %subject.', array('%subject' => $comment->subject), WATCHDOG_WARNING);
    drupal_set_message(t('Comment: unauthorized comment submitted or comment submitted to a closed post %subject.', array('%subject' => $comment->subject)), 'error');
    // Redirect the user to the node they are commenting on.
    $redirect = 'node/' . $node->nid;
  }
  $form_state['redirect'] = $redirect;
  // Clear the block and page caches so that anonymous users see the comment
  // they have posted.
  cache_clear_all();
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
