# node_search_status()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 1663–1667 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L1663-L1667)
- **Module/theme:** node
- **Implements:** [hook_search_status()](../../search/search.api.php/hook_search_status.md)

## Signature

```php
function node_search_status()
```

## Documentation

```text
Implements hook_search_status().
```

## Code

```php
function node_search_status() {
  $total = db_query('SELECT COUNT(*) FROM {node}')->fetchField();
  $remaining = db_query("SELECT COUNT(*) FROM {node} n LEFT JOIN {search_dataset} d ON d.type = 'node' AND d.sid = n.nid WHERE d.sid IS NULL OR d.reindex <> 0")->fetchField();
  return array('remaining' => $remaining, 'total' => $total);
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
