# _forum_topics_unread()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 883–895 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L883-L895)
- **Module/theme:** forum

## Signature

```php
function _forum_topics_unread($term, $uid)
```

## Documentation

```text
Calculates the number of new posts in a forum that the user has not yet read.

Nodes are new if they are newer than NODE_NEW_LIMIT.

@param $term
  The term ID of the forum.
@param $uid
  The user ID.

@return
  The number of new posts in the forum that have not been read by the user.
```

## Code

```php
function _forum_topics_unread($term, $uid) {
  $query = db_select('node', 'n');
  $query->join('forum', 'f', 'n.vid = f.vid AND f.tid = :tid', array(':tid' => $term));
  $query->leftJoin('history', 'h', 'n.nid = h.nid AND h.uid = :uid', array(':uid' => $uid));
  $query->addExpression('COUNT(n.nid)', 'count');
  return $query
    ->condition('status', 1)
    ->condition('n.created', NODE_NEW_LIMIT, '>')
    ->isNull('h.nid')
    ->addTag('node_access')
    ->execute()
    ->fetchField();
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
