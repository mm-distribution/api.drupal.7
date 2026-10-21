# node_type_cache_reset()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 784–787 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L784-L787)
- **Module/theme:** node

## Signature

```php
function node_type_cache_reset()
```

## Documentation

```text
Clears the node type cache.
```

## Code

```php
function node_type_cache_reset() {
  cache_clear_all('node_types:', 'cache', TRUE);
  drupal_static_reset('_node_types_build');
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
