# node_type_get_types()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 393–395 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L393-L395)
- **Module/theme:** node

## Signature

```php
function node_type_get_types()
```

## Documentation

```text
Returns a list of all the available node types.

This list can include types that are queued for addition or deletion.
See _node_types_build() for details.

@return
  An array of node types, as objects, keyed by the type.

@see node_type_get_type()
```

## Code

```php
function node_type_get_types() {
  return _node_types_build()->types;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
