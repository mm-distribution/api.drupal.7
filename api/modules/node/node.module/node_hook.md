# node_hook()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 894–897 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L894-L897)
- **Module/theme:** node

## Signature

```php
function node_hook($node, $hook)
```

## Documentation

```text
Determines whether a node hook exists.

@param $node
  A node object or a string containing the node type.
@param $hook
  A string containing the name of the hook.

@return
  TRUE if the $hook exists in the node type of $node.
```

## Code

```php
function node_hook($node, $hook) {
  $base = node_type_get_base($node);
  return module_hook($base, $hook);
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
