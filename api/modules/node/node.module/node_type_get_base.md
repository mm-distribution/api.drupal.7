# node_type_get_base()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 431–435 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L431-L435)
- **Module/theme:** node

## Signature

```php
function node_type_get_base($node)
```

## Documentation

```text
Returns the node type base of the passed node or node type string.

The base indicates which module implements this node type and is used to
execute node-type-specific hooks. For types defined in the user interface
and managed by node.module, the base is 'node_content'.

@param $node
  A node object or string that indicates the node type to return.

@return
  The node type base or FALSE if the node type is not found.

@see node_invoke()
```

## Code

```php
function node_type_get_base($node) {
  $type = _node_extract_type($node);
  $types = _node_types_build()->types;
  return isset($types[$type]) && isset($types[$type]->base) ? $types[$type]->base : FALSE;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
