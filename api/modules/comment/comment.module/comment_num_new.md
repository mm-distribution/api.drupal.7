# comment_num_new()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 1744–1765 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L1744-L1765)
- **Module/theme:** comment

## Signature

```php
function comment_num_new($nid, $timestamp = 0)
```

## Documentation

```text
Get number of new comments for current user and specified node.

@param $nid
  Node-id to count comments for.
@param $timestamp
  Time to count from (defaults to time of last user access
  to node).
@return The result or FALSE on error.
```

## Code

```php
function comment_num_new($nid, $timestamp = 0) {
  global $user;

  if ($user->uid) {
    // Retrieve the timestamp at which the current user last viewed this node.
    if (!$timestamp) {
      $timestamp = node_last_viewed($nid);
    }
    $timestamp = ($timestamp > NODE_NEW_LIMIT ? $timestamp : NODE_NEW_LIMIT);

    // Use the timestamp to retrieve the number of new comments.
    return db_query('SELECT COUNT(cid) FROM {comment} WHERE nid = :nid AND created > :timestamp AND status = :status', array(
      ':nid' => $nid,
      ':timestamp' => $timestamp,
      ':status' => COMMENT_PUBLISHED,
      ))->fetchField();
  }
  else {
    return FALSE;
  }

}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
