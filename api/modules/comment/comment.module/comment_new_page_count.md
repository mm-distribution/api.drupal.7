# comment_new_page_count()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 537–590 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L537-L590)
- **Module/theme:** comment

## Signature

```php
function comment_new_page_count($num_comments, $new_replies, $node)
```

## Documentation

```text
Calculate page number for first new comment.

@param $num_comments
  Number of comments.
@param $new_replies
  Number of new replies.
@param $node
  The first new comment node.
@return
  "page=X" if the page number is greater than zero; empty string otherwise.
```

## Code

```php
function comment_new_page_count($num_comments, $new_replies, $node) {
  $mode = variable_get('comment_default_mode_' . $node->type, COMMENT_MODE_THREADED);
  $comments_per_page = variable_get('comment_default_per_page_' . $node->type, 50);
  $pagenum = NULL;
  $flat = $mode == COMMENT_MODE_FLAT ? TRUE : FALSE;
  if ($num_comments <= $comments_per_page) {
    // Only one page of comments.
    $pageno = 0;
  }
  elseif ($flat) {
    // Flat comments.
    $count = $num_comments - $new_replies;
    $pageno = $count / $comments_per_page;
  }
  else {
    // Threaded comments: we build a query with a subquery to find the first
    // thread with a new comment.

    // 1. Find all the threads with a new comment.
    $unread_threads_query = db_select('comment')
      ->fields('comment', array('thread'))
      ->condition('nid', $node->nid)
      ->condition('status', COMMENT_PUBLISHED)
      ->orderBy('created', 'DESC')
      ->orderBy('cid', 'DESC')
      ->range(0, $new_replies);

    // 2. Find the first thread.
    $first_thread = db_select($unread_threads_query, 'thread')
      ->fields('thread', array('thread'))
      ->orderBy('SUBSTRING(thread, 1, (LENGTH(thread) - 1))')
      ->range(0, 1)
      ->execute()
      ->fetchField();

    // Remove the final '/'.
    $first_thread = substr($first_thread, 0, -1);

    // Find the number of the first comment of the first unread thread.
    $count = db_query('SELECT COUNT(*) FROM {comment} WHERE nid = :nid AND status = :status AND SUBSTRING(thread, 1, (LENGTH(thread) - 1)) < :thread', array(
      ':status' => COMMENT_PUBLISHED,
      ':nid' => $node->nid,
      ':thread' => $first_thread,
    ))->fetchField();

    $pageno = $count / $comments_per_page;
  }

  if ($pageno >= 1) {
    $pagenum = array('page' => intval($pageno));
  }

  return $pagenum;
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
