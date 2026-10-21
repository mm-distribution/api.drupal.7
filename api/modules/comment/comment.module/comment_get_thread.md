# comment_get_thread()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 828–865 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L828-L865)
- **Module/theme:** comment

## Signature

```php
function comment_get_thread($node, $mode, $comments_per_page)
```

## Documentation

```text
Retrieve comments for a thread.

@param $node
  The node whose comment(s) needs rendering.
@param $mode
  The comment display mode; COMMENT_MODE_FLAT or COMMENT_MODE_THREADED.
@param $comments_per_page
  The amount of comments to display per page.

To display threaded comments in the correct order we keep a 'thread' field
and order by that value. This field keeps this data in
a way which is easy to update and convenient to use.

A "thread" value starts at "1". If we add a child (A) to this comment,
we assign it a "thread" = "1.1". A child of (A) will have "1.1.1". Next
brother of (A) will get "1.2". Next brother of the parent of (A) will get
"2" and so on.

First of all note that the thread field stores the depth of the comment:
depth 0 will be "X", depth 1 "X.X", depth 2 "X.X.X", etc.

Now to get the ordering right, consider this example:

1
1.1
1.1.1
1.2
2

If we "ORDER BY thread ASC" we get the above result, and this is the
natural order sorted by time. However, if we "ORDER BY thread DESC"
we get:

2
1.2
1.1.1
1.1
1

Clearly, this is not a natural way to see a thread, and users will get
confused. The natural order to show a thread by time desc would be:

2
1
1.2
1.1
1.1.1

which is what we already did before the standard pager patch. To achieve
this we simply add a "/" at the end of each "thread" value. This way, the
thread fields will look like this:

1/
1.1/
1.1.1/
1.2/
2/

we add "/" since this char is, in ASCII, higher than every number, so if
now we "ORDER BY thread DESC" we get the correct order. However this would
spoil the reverse ordering, "ORDER BY thread ASC" -- here, we do not need
to consider the trailing "/" so we use a substring only.
```

## Code

```php
function comment_get_thread($node, $mode, $comments_per_page) {
  $query = db_select('comment', 'c')->extend('PagerDefault');
  $query->addField('c', 'cid');
  $query
    ->condition('c.nid', $node->nid)
    ->addTag('node_access')
    ->addTag('comment_filter')
    ->addMetaData('node', $node)
    ->limit($comments_per_page);

  $count_query = db_select('comment', 'c');
  $count_query->addExpression('COUNT(*)');
  $count_query
    ->condition('c.nid', $node->nid)
    ->addTag('node_access')
    ->addTag('comment_filter')
    ->addMetaData('node', $node);

  if (!user_access('administer comments')) {
    $query->condition('c.status', COMMENT_PUBLISHED);
    $count_query->condition('c.status', COMMENT_PUBLISHED);
  }
  if ($mode === COMMENT_MODE_FLAT) {
    $query->orderBy('c.cid', 'ASC');
  }
  else {
    // See comment above. Analysis reveals that this doesn't cost too
    // much. It scales much much better than having the whole comment
    // structure.
    $query->addExpression('SUBSTRING(c.thread, 1, (LENGTH(c.thread) - 1))', 'torder');
    $query->orderBy('torder', 'ASC');
  }

  $query->setCountQuery($count_query);
  $cids = $query->execute()->fetchCol();

  return $cids;
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
