# taxonomy_node_insert()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 1916–1919 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L1916-L1919)
- **Module/theme:** taxonomy
- **Topics:** [taxonomy_index](../../../topics/taxonomy_index.md)
- **Implements:** [hook_node_insert()](../../node/node.api.php/hook_node_insert.md)

## Signature

```php
function taxonomy_node_insert($node)
```

## Documentation

```text
Implements hook_node_insert().
```

## Code

```php
function taxonomy_node_insert($node) {
  // Add taxonomy index entries for the node.
  taxonomy_build_node_index($node);
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
