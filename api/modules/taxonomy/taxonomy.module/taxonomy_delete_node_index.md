# taxonomy_delete_node_index()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 2013–2017 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L2013-L2017)
- **Module/theme:** taxonomy
- **Topics:** [taxonomy_index](../../../topics/taxonomy_index.md)

## Signature

```php
function taxonomy_delete_node_index($node)
```

## Documentation

```text
Deletes taxonomy index entries for a given node.

@param $node
  The node object.
```

## Code

```php
function taxonomy_delete_node_index($node) {
  if (variable_get('taxonomy_maintain_index_table', TRUE)) {
    db_delete('taxonomy_index')->condition('nid', $node->nid)->execute();
  }
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
