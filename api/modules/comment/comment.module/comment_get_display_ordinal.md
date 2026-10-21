# comment_get_display_ordinal()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 1781–1807 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L1781-L1807)
- **Module/theme:** comment

## Signature

```php
function comment_get_display_ordinal($cid, $node_type)
```

## Documentation

```text
Get the display ordinal for a comment, starting from 0.

Count the number of comments which appear before the comment we want to
display, taking into account display settings and threading.

@param $cid
  The comment ID.
@param $node_type
  The node type of the comment's parent.
@return
  The display ordinal for the comment.
@see comment_get_display_page()
```

## Code

```php
function comment_get_display_ordinal($cid, $node_type) {
  // Count how many comments (c1) are before $cid (c2) in display order. This is
  // the 0-based display ordinal.
  $query = db_select('comment', 'c1');
  $query->innerJoin('comment', 'c2', 'c2.nid = c1.nid');
  $query->addExpression('COUNT(*)', 'count');
  $query->condition('c2.cid', $cid);
  if (!user_access('administer comments')) {
    $query->condition('c1.status', COMMENT_PUBLISHED);
  }
  $mode = variable_get('comment_default_mode_' . $node_type, COMMENT_MODE_THREADED);

  if ($mode == COMMENT_MODE_FLAT) {
    // For flat comments, cid is used for ordering comments due to
    // unpredicatable behavior with timestamp, so we make the same assumption
    // here.
    $query->condition('c1.cid', $cid, '<');
  }
  else {
    // For threaded comments, the c.thread column is used for ordering. We can
    // use the vancode for comparison, but must remove the trailing slash.
    // See comment_view_multiple().
    $query->where('SUBSTRING(c1.thread, 1, (LENGTH(c1.thread) -1)) < SUBSTRING(c2.thread, 1, (LENGTH(c2.thread) -1))');
  }

  return $query->execute()->fetchField();
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
