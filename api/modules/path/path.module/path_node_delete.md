# path_node_delete()

- **Type:** Function
- **File:** [`modules/path/path.module`](_file.md), lines 221–224 · [local source](../../../../source/modules/path/path.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.module#L221-L224)
- **Module/theme:** path
- **Implements:** [hook_node_delete()](../../node/node.api.php/hook_node_delete.md)

## Signature

```php
function path_node_delete($node)
```

## Documentation

```text
Implements hook_node_delete().
```

## Code

```php
function path_node_delete($node) {
  // Delete all aliases associated with this node.
  path_delete(array('source' => 'node/' . $node->nid));
}
```

---
_Drupal 7.103 · [modules/path/path.module](https://github.com/drupal/drupal/blob/7.103/modules/path/path.module) · Licensed GPL-2.0-or-later (see LICENSE)._
