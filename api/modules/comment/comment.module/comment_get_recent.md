# comment_get_recent()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 506–523 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L506-L523)
- **Module/theme:** comment

## Signature

```php
function comment_get_recent($number = 10)
```

## Documentation

```text
Find the most recent comments that are available to the current user.

@param integer $number
  (optional) The maximum number of comments to find. Defaults to 10.

@return
  An array of comment objects or an empty array if there are no recent
  comments visible to the current user.
```

## Code

```php
function comment_get_recent($number = 10) {
  $query = db_select('comment', 'c');
  $query->innerJoin('node', 'n', 'n.nid = c.nid');
  $query->addTag('node_access');
  $comments = $query
    ->fields('c')
    ->condition('c.status', COMMENT_PUBLISHED)
    ->condition('n.status', NODE_PUBLISHED)
    ->orderBy('c.created', 'DESC')
    // Additionally order by cid to ensure that comments with the same timestamp
    // are returned in the exact order posted.
    ->orderBy('c.cid', 'DESC')
    ->range(0, $number)
    ->execute()
    ->fetchAll();

  return $comments ? $comments : array();
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
