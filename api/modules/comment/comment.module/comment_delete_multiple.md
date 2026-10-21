# comment_delete_multiple()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 1631–1657 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L1631-L1657)
- **Module/theme:** comment

## Signature

```php
function comment_delete_multiple($cids)
```

## Documentation

```text
Delete comments and all their replies.

@param $cids
  The comment to delete.
```

## Code

```php
function comment_delete_multiple($cids) {
  $comments = comment_load_multiple($cids);
  if ($comments) {
    $transaction = db_transaction();
    try {
      // Delete the comments.
      db_delete('comment')
        ->condition('cid', array_keys($comments), 'IN')
        ->execute();
      foreach ($comments as $comment) {
        field_attach_delete('comment', $comment);
        module_invoke_all('comment_delete', $comment);
        module_invoke_all('entity_delete', $comment, 'comment');

        // Delete the comment's replies.
        $child_cids = db_query('SELECT cid FROM {comment} WHERE pid = :cid', array(':cid' => $comment->cid))->fetchCol();
        comment_delete_multiple($child_cids);
        _comment_update_node_statistics($comment->nid);
      }
    }
    catch (Exception $e) {
      $transaction->rollback();
      watchdog_exception('comment', $e);
      throw $e;
    }
  }
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
