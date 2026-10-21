# node_invoke()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 912–918 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L912-L918)
- **Module/theme:** node

## Signature

```php
function node_invoke($node, $hook, $a2 = NULL, $a3 = NULL, $a4 = NULL)
```

## Documentation

```text
Invokes a node hook.

@param $node
  A node object or a string containing the node type.
@param $hook
  A string containing the name of the hook.
@param $a2, $a3, $a4
  Arguments to pass on to the hook, after the $node argument.

@return
  The returned value of the invoked hook.
```

## Code

```php
function node_invoke($node, $hook, $a2 = NULL, $a3 = NULL, $a4 = NULL) {
  if (node_hook($node, $hook)) {
    $base = node_type_get_base($node);
    $function = $base . '_' . $hook;
    return ($function($node, $a2, $a3, $a4));
  }
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
