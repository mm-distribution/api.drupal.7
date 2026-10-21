# hook_prepare()

- **Type:** Hook (documentation function)
- **File:** [`modules/node/node.api.php`](_file.md), lines 1086–1090 · [local source](../../../../source/modules/node/node.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php#L1086-L1090)
- **Module/theme:** node
- **Topics:** [hooks](../../../topics/hooks.md), [node_api_hooks](../../../topics/node_api_hooks.md)

## Signature

```php
function hook_prepare($node)
```

## Documentation

```text
Act on a node object about to be shown on the add/edit form.

This is a node-type-specific hook, which is invoked only for the node type
being affected. See
@link node_api_hooks Node API hooks @endlink for more information.

Use hook_node_prepare() to respond to node preparation of all node types.

This hook is invoked from node_object_prepare() before the general
hook_node_prepare() is invoked.

@param $node
  The node that is about to be shown on the add/edit form.

@ingroup node_api_hooks
```

## Code

```php
function hook_prepare($node) {
  if (!isset($node->mymodule_value)) {
    $node->mymodule_value = 'foo';
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_prepare()".

_None found._

---
_Drupal 7.103 · [modules/node/node.api.php](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
