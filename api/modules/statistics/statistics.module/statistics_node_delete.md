# statistics_node_delete()

- **Type:** Function
- **File:** [`modules/statistics/statistics.module`](_file.md), lines 428–433 · [local source](../../../../source/modules/statistics/statistics.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module#L428-L433)
- **Module/theme:** statistics
- **Implements:** [hook_node_delete()](../../node/node.api.php/hook_node_delete.md)

## Signature

```php
function statistics_node_delete($node)
```

## Documentation

```text
Implements hook_node_delete().
```

## Code

```php
function statistics_node_delete($node) {
  // clean up statistics table when node is deleted
  db_delete('node_counter')
    ->condition('nid', $node->nid)
    ->execute();
}
```

---
_Drupal 7.103 · [modules/statistics/statistics.module](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module) · Licensed GPL-2.0-or-later (see LICENSE)._
