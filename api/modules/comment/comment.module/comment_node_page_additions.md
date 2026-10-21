# comment_node_page_additions()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 722–762 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L722-L762)
- **Module/theme:** comment

## Signature

```php
function comment_node_page_additions($node)
```

## Documentation

```text
Build the comment-related elements for node detail pages.

@param $node
 A node object.
```

## Code

```php
function comment_node_page_additions($node) {
  $additions = array();

  // Only attempt to render comments if the node has visible comments.
  // Unpublished comments are not included in $node->comment_count, so show
  // comments unconditionally if the user is an administrator.
  if (($node->comment_count && user_access('access comments')) || user_access('administer comments')) {
    $mode = variable_get('comment_default_mode_' . $node->type, COMMENT_MODE_THREADED);
    $comments_per_page = variable_get('comment_default_per_page_' . $node->type, 50);
    if ($cids = comment_get_thread($node, $mode, $comments_per_page)) {
      $comments = comment_load_multiple($cids);
      if ($comments) {
        comment_prepare_thread($comments);
        $build = comment_view_multiple($comments, $node);
        $build['pager']['#theme'] = 'pager';
        $additions['comments'] = $build;
      }
      elseif ($node->comment_count > 0) {
        // Comment count has got out of line, update it.
        db_query("UPDATE {node_comment_statistics} SET comment_count = 0 WHERE nid = :nid", array(':nid' => $node->nid));
      }
    }
  }

  // Append comment form if needed.
  if (user_access('post comments') && $node->comment == COMMENT_NODE_OPEN && (variable_get('comment_form_location_' . $node->type, COMMENT_FORM_BELOW) == COMMENT_FORM_BELOW)) {
    $build = drupal_get_form("comment_node_{$node->type}_form", (object) array('nid' => $node->nid));
    $additions['comment_form'] = $build;
  }

  if ($additions) {
    $additions += array(
      '#theme' => 'comment_wrapper__node_' . $node->type,
      '#node' => $node,
      'comments' => array(),
      'comment_form' => array(),
    );
  }

  return $additions;
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
