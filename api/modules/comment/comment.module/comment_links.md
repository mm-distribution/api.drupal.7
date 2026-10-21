# comment_links()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 1043–1091 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L1043-L1091)
- **Module/theme:** comment

## Signature

```php
function comment_links($comment, $node)
```

## Documentation

```text
Helper function, build links for an individual comment.

Adds reply, edit, delete etc. depending on the current user permissions.

@param $comment
  The comment object.
@param $node
  The node the comment is attached to.
@return
  A structured array of links.
```

## Code

```php
function comment_links($comment, $node) {
  $links = array();
  if ($node->comment == COMMENT_NODE_OPEN) {
    if (user_access('administer comments') && user_access('post comments')) {
      $links['comment-delete'] = array(
        'title' => t('delete'),
        'href' => "comment/$comment->cid/delete",
        'html' => TRUE,
      );
      $links['comment-edit'] = array(
        'title' => t('edit'),
        'href' => "comment/$comment->cid/edit",
        'html' => TRUE,
      );
      $links['comment-reply'] = array(
        'title' => t('reply'),
        'href' => "comment/reply/$comment->nid/$comment->cid",
        'html' => TRUE,
      );
      if ($comment->status == COMMENT_NOT_PUBLISHED) {
        $links['comment-approve'] = array(
          'title' => t('approve'),
          'href' => "comment/$comment->cid/approve",
          'html' => TRUE,
          'query' => array('token' => drupal_get_token("comment/$comment->cid/approve")),
        );
      }
    }
    elseif (user_access('post comments')) {
      if (comment_access('edit', $comment)) {
        $links['comment-edit'] = array(
          'title' => t('edit'),
          'href' => "comment/$comment->cid/edit",
          'html' => TRUE,
        );
      }
      $links['comment-reply'] = array(
        'title' => t('reply'),
        'href' => "comment/reply/$comment->nid/$comment->cid",
        'html' => TRUE,
      );
    }
    else {
      $links['comment_forbidden']['title'] = theme('comment_post_forbidden', array('node' => $node));
      $links['comment_forbidden']['html'] = TRUE;
    }
  }
  return $links;
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
