# node_type_delete()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 652–662 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L652-L662)
- **Module/theme:** node

## Signature

```php
function node_type_delete($type)
```

## Documentation

```text
Deletes a node type from the database.

@param $type
  The machine-readable name of the node type to be deleted.
```

## Code

```php
function node_type_delete($type) {
  $info = node_type_get_type($type);
  db_delete('node_type')
    ->condition('type', $type)
    ->execute();
  field_attach_delete_bundle('node', $type);
  module_invoke_all('node_type_delete', $info);

  // Clear the node type cache.
  node_type_cache_reset();
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
