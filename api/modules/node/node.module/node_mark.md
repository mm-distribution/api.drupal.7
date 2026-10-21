# node_mark()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 350–367 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L350-L367)
- **Module/theme:** node

## Signature

```php
function node_mark($nid, $timestamp)
```

## Documentation

```text
Determines the type of marker to be displayed for a given node.

@param $nid
  Node ID whose history supplies the "last viewed" timestamp.
@param $timestamp
  Time which is compared against node's "last viewed" timestamp.

@return
  One of the MARK constants.
```

## Code

```php
function node_mark($nid, $timestamp) {
  global $user;
  $cache = &drupal_static(__FUNCTION__, array());

  if (!$user->uid) {
    return MARK_READ;
  }
  if (!isset($cache[$nid])) {
    $cache[$nid] = node_last_viewed($nid);
  }
  if ($cache[$nid] == 0 && $timestamp > NODE_NEW_LIMIT) {
    return MARK_NEW;
  }
  elseif ($timestamp > $cache[$nid] && $timestamp > NODE_NEW_LIMIT) {
    return MARK_UPDATED;
  }
  return MARK_READ;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
