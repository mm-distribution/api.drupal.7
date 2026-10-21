# node_update_index()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 2767–2775 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L2767-L2775)
- **Module/theme:** node
- **Implements:** [hook_update_index()](../../search/search.api.php/hook_update_index.md)

## Signature

```php
function node_update_index()
```

## Documentation

```text
Implements hook_update_index().
```

## Code

```php
function node_update_index() {
  $limit = (int)variable_get('search_cron_limit', 100);

  $result = db_query_range("SELECT n.nid FROM {node} n LEFT JOIN {search_dataset} d ON d.type = 'node' AND d.sid = n.nid WHERE d.sid IS NULL OR d.reindex <> 0 ORDER BY d.reindex ASC, n.nid ASC", 0, $limit, array(), array('target' => 'slave'));

  foreach ($result as $node) {
    _node_index_node($node);
  }
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
