# path_node_update()

- **Type:** Function
- **File:** [`modules/path/path.module`](_file.md), lines 206–216 · [local source](../../../../source/modules/path/path.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.module#L206-L216)
- **Module/theme:** path
- **Implements:** [hook_node_update()](../../node/node.api.php/hook_node_update.md)

## Signature

```php
function path_node_update($node)
```

## Documentation

```text
Implements hook_node_update().
```

## Code

```php
function path_node_update($node) {
  if (isset($node->path)) {
    $path = $node->path;
    $path['alias'] = isset($path['alias']) ? trim($path['alias']) : '';
    // Delete old alias if user erased it.
    if (!empty($path['pid']) && !$path['alias']) {
      path_delete($path['pid']);
    }
    path_node_insert($node);
  }
}
```

---
_Drupal 7.103 · [modules/path/path.module](https://github.com/drupal/drupal/blob/7.103/modules/path/path.module) · Licensed GPL-2.0-or-later (see LICENSE)._
