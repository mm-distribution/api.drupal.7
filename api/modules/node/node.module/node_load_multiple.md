# node_load_multiple()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 946–948 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L946-L948)
- **Module/theme:** node

## Signature

```php
function node_load_multiple($nids = array(), $conditions = array(), $reset = FALSE)
```

## Documentation

```text
Loads node entities from the database.

This function should be used whenever you need to load more than one node
from the database. Nodes are loaded into memory and will not require database
access if loaded again during the same page request.

@see entity_load()
@see EntityFieldQuery

@param $nids
  An array of node IDs.
@param $conditions
  (deprecated) An associative array of conditions on the {node}
  table, where the keys are the database fields and the values are the
  values those fields must have. Instead, it is preferable to use
  EntityFieldQuery to retrieve a list of entity IDs loadable by
  this function.
@param $reset
  Whether to reset the internal node_load cache.

@return
  An array of node objects indexed by nid.

@todo Remove $conditions in Drupal 8.
```

## Code

```php
function node_load_multiple($nids = array(), $conditions = array(), $reset = FALSE) {
  return entity_load('node', $nids, $conditions, $reset);
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
