# node_last_changed()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 2212–2214 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L2212-L2214)
- **Module/theme:** node

## Signature

```php
function node_last_changed($nid)
```

## Documentation

```text
Finds the last time a node was changed.

@param $nid
  The ID of a node.

@return
  A unix timestamp indicating the last time the node was changed.
```

## Code

```php
function node_last_changed($nid) {
  return db_query('SELECT changed FROM {node} WHERE nid = :nid', array(':nid' => $nid))->fetch()->changed;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
