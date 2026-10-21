# comment_node_update_index()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 1342–1377 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L1342-L1377)
- **Module/theme:** comment
- **Implements:** [hook_node_update_index()](../../node/node.api.php/hook_node_update_index.md)

## Signature

```php
function comment_node_update_index($node)
```

## Documentation

```text
Implements hook_node_update_index().
```

## Code

```php
function comment_node_update_index($node) {
  $index_comments = &drupal_static(__FUNCTION__);

  if ($index_comments === NULL) {
    // Find and save roles that can 'access comments' or 'search content'.
    $perms = array('access comments' => array(), 'search content' => array());
    $result = db_query("SELECT rid, permission FROM {role_permission} WHERE permission IN ('access comments', 'search content')");
    foreach ($result as $record) {
      $perms[$record->permission][$record->rid] = $record->rid;
    }

    // Prevent indexing of comments if there are any roles that can search but
    // not view comments.
    $index_comments = TRUE;
    foreach ($perms['search content'] as $rid) {
      if (!isset($perms['access comments'][$rid]) && ($rid <= DRUPAL_AUTHENTICATED_RID || !isset($perms['access comments'][DRUPAL_AUTHENTICATED_RID]))) {
        $index_comments = FALSE;
        break;
      }
    }
  }

  if ($index_comments) {
    $mode = variable_get('comment_default_mode_' . $node->type, COMMENT_MODE_THREADED);
    $comments_per_page = variable_get('comment_default_per_page_' . $node->type, 50);
    if ($node->comment && $cids = comment_get_thread($node, $mode, $comments_per_page)) {
      $comments = comment_load_multiple($cids);
      if ($comments) {
        comment_prepare_thread($comments);
        $build = comment_view_multiple($comments, $node);
        return drupal_render($build);
      }
    }
  }
  return '';
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
