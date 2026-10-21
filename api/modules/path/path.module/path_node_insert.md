# path_node_insert()

- **Type:** Function
- **File:** [`modules/path/path.module`](_file.md), lines 188–201 · [local source](../../../../source/modules/path/path.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.module#L188-L201)
- **Module/theme:** path
- **Implements:** [hook_node_insert()](../../node/node.api.php/hook_node_insert.md)

## Signature

```php
function path_node_insert($node)
```

## Documentation

```text
Implements hook_node_insert().
```

## Code

```php
function path_node_insert($node) {
  if (isset($node->path) && isset($node->path['alias'])) {
    $path = $node->path;
    $path['alias'] = trim($path['alias']);
    // Only save a non-empty alias.
    if (!empty($path['alias'])) {
      // Ensure fields for programmatic executions.
      $langcode = entity_language('node', $node);
      $path['source'] = 'node/' . $node->nid;
      $path['language'] = isset($langcode) ? $langcode : LANGUAGE_NONE;
      path_save($path);
    }
  }
}
```

---
_Drupal 7.103 · [modules/path/path.module](https://github.com/drupal/drupal/blob/7.103/modules/path/path.module) · Licensed GPL-2.0-or-later (see LICENSE)._
