# node_type_update_nodes()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 675–680 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L675-L680)
- **Module/theme:** node

## Signature

```php
function node_type_update_nodes($old_type, $type)
```

## Documentation

```text
Updates all nodes of one type to be of another type.

@param $old_type
  The current node type of the nodes.
@param $type
  The new node type of the nodes.

@return
  The number of nodes whose node type field was modified.
```

## Code

```php
function node_type_update_nodes($old_type, $type) {
  return db_update('node')
    ->fields(array('type' => $type))
    ->condition('type', $old_type)
    ->execute();
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
