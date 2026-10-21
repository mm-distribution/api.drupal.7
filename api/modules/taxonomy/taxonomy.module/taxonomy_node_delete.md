# taxonomy_node_delete()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 2002–2005 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L2002-L2005)
- **Module/theme:** taxonomy
- **Topics:** [taxonomy_index](../../../topics/taxonomy_index.md)
- **Implements:** [hook_node_delete()](../../node/node.api.php/hook_node_delete.md)

## Signature

```php
function taxonomy_node_delete($node)
```

## Documentation

```text
Implements hook_node_delete().
```

## Code

```php
function taxonomy_node_delete($node) {
  // Clean up the {taxonomy_index} table when nodes are deleted.
  taxonomy_delete_node_index($node);
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
