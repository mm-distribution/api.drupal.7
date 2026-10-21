# node_permissions_get_configured_types()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 3181–3192 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L3181-L3192)
- **Module/theme:** node
- **Topics:** [node_access](../../../topics/node_access.md)

## Signature

```php
function node_permissions_get_configured_types()
```

## Documentation

```text
Returns an array of node types that should be managed by permissions.

By default, this will include all node types in the system. To exclude a
specific node from getting permissions defined for it, set the
node_permissions_$type variable to 0. Core does not provide an interface for
doing so. However, contrib modules may exclude their own nodes in
hook_install(). Alternatively, contrib modules may configure all node types
at once, or decide to apply some other hook_node_access() implementation to
some or all node types.

@return
  An array of node types managed by this module.
```

## Code

```php
function node_permissions_get_configured_types() {

  $configured_types = array();

  foreach (node_type_get_types() as $type => $info) {
    if (variable_get('node_permissions_' . $type, 1)) {
      $configured_types[] = $type;
    }
  }

  return $configured_types;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
