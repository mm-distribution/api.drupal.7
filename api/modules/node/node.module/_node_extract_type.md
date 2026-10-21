# _node_extract_type()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 378–380 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L378-L380)
- **Module/theme:** node

## Signature

```php
function _node_extract_type($node)
```

## Documentation

```text
Extracts the type name.

@param $node
  Either a string or object, containing the node type information.

@return
  Node type of the passed-in data.
```

## Code

```php
function _node_extract_type($node) {
  return is_object($node) ? $node->type : $node;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
