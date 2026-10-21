# node_type_get_type()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 410–414 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L410-L414)
- **Module/theme:** node

## Signature

```php
function node_type_get_type($node)
```

## Documentation

```text
Returns the node type of the passed node or node type string.

@param $node
  A node object or string that indicates the node type to return.

@return
  A single node type, as an object, or FALSE if the node type is not found.
  The node type is an object containing fields from hook_node_info() return
  values, as well as the field 'type' (the machine-readable type) and other
  fields used internally and defined in _node_types_build(),
  hook_node_info(), and node_type_set_defaults().
```

## Code

```php
function node_type_get_type($node) {
  $type = _node_extract_type($node);
  $types = _node_types_build()->types;
  return isset($types[$type]) ? $types[$type] : FALSE;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
