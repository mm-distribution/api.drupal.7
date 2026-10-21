# _forum_user_last_visit()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 1289–1300 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L1289-L1300)
- **Module/theme:** forum

## Signature

```php
function _forum_user_last_visit($nid)
```

## Documentation

```text
Gets the last time the user viewed a node.

@param $nid
  The node ID.

@return
  The timestamp when the user last viewed this node, if the user has
  previously viewed the node; otherwise NODE_NEW_LIMIT.
```

## Code

```php
function _forum_user_last_visit($nid) {
  global $user;
  $history = &drupal_static(__FUNCTION__, array());

  if (empty($history)) {
    $result = db_query('SELECT nid, timestamp FROM {history} WHERE uid = :uid', array(':uid' => $user->uid));
    foreach ($result as $t) {
      $history[$t->nid] = $t->timestamp > NODE_NEW_LIMIT ? $t->timestamp : NODE_NEW_LIMIT;
    }
  }
  return isset($history[$nid]) ? $history[$nid] : NODE_NEW_LIMIT;
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
