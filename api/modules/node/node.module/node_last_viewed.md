# node_last_viewed()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 328–337 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L328-L337)
- **Module/theme:** node

## Signature

```php
function node_last_viewed($nid)
```

## Documentation

```text
Retrieves the timestamp for the current user's last view of a specified node.

@param $nid
  A node ID.

@return
  If a node has been previously viewed by the user, the timestamp in seconds
  of when the last view occurred; otherwise, zero.
```

## Code

```php
function node_last_viewed($nid) {
  global $user;
  $history = &drupal_static(__FUNCTION__, array());

  if (!isset($history[$nid])) {
    $history[$nid] = db_query("SELECT timestamp FROM {history} WHERE uid = :uid AND nid = :nid", array(':uid' => $user->uid, ':nid' => $nid))->fetchObject();
  }

  return (isset($history[$nid]->timestamp) ? $history[$nid]->timestamp : 0);
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
