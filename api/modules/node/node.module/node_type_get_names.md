# node_type_get_names()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 446–448 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L446-L448)
- **Module/theme:** node

## Signature

```php
function node_type_get_names()
```

## Documentation

```text
Returns a list of available node type names.

This list can include types that are queued for addition or deletion.
See _node_types_build() for details.

@return
  An array of node type names, keyed by the type.
```

## Code

```php
function node_type_get_names() {
  return _node_types_build()->names;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
