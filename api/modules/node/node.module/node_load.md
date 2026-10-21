# node_load()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 963–968 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L963-L968)
- **Module/theme:** node

## Signature

```php
function node_load($nid = NULL, $vid = NULL, $reset = FALSE)
```

## Documentation

```text
Loads a node object from the database.

@param $nid
  The node ID.
@param $vid
  The revision ID.
@param $reset
  Whether to reset the node_load_multiple cache.

@return
  A fully-populated node object, or FALSE if the node is not found.
```

## Code

```php
function node_load($nid = NULL, $vid = NULL, $reset = FALSE) {
  $nids = (isset($nid) ? array($nid) : array());
  $conditions = (isset($vid) ? array('vid' => $vid) : array());
  $node = node_load_multiple($nids, $conditions, $reset);
  return $node ? reset($node) : FALSE;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
