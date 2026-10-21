# node_type_get_name()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 459–463 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L459-L463)
- **Module/theme:** node

## Signature

```php
function node_type_get_name($node)
```

## Documentation

```text
Returns the node type name of the passed node or node type string.

@param $node
  A node object or string that indicates the node type to return.

@return
  The node type name or FALSE if the node type is not found.
```

## Code

```php
function node_type_get_name($node) {
  $type = _node_extract_type($node);
  $types = _node_types_build()->names;
  return isset($types[$type]) ? $types[$type] : FALSE;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
