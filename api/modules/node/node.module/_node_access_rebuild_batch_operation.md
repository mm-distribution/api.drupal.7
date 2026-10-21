# _node_access_rebuild_batch_operation()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 3688–3714 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L3688-L3714)
- **Module/theme:** node
- **Topics:** [node_access](../../../topics/node_access.md)

## Signature

```php
function _node_access_rebuild_batch_operation(&$context)
```

## Documentation

```text
Implements callback_batch_operation().

Performs batch operation for node_access_rebuild().

This is a multistep operation: we go through all nodes by packs of 20. The
batch processing engine interrupts processing and sends progress feedback
after 1 second execution time.

@param array $context
  An array of contextual key/value information for rebuild batch process.
```

## Code

```php
function _node_access_rebuild_batch_operation(&$context) {
  if (empty($context['sandbox'])) {
    // Initiate multistep processing.
    $context['sandbox']['progress'] = 0;
    $context['sandbox']['current_node'] = 0;
    $context['sandbox']['max'] = db_query('SELECT COUNT(nid) FROM {node}')->fetchField();
  }

  // Process the next 20 nodes.
  $limit = 20;
  $nids = db_query_range("SELECT nid FROM {node} WHERE nid > :nid ORDER BY nid ASC", 0, $limit, array(':nid' => $context['sandbox']['current_node']))->fetchCol();
  $nodes = node_load_multiple($nids, array(), TRUE);
  foreach ($nodes as $nid => $node) {
    // To preserve database integrity, only acquire grants if the node
    // loads successfully.
    if (!empty($node)) {
      node_access_acquire_grants($node);
    }
    $context['sandbox']['progress']++;
    $context['sandbox']['current_node'] = $nid;
  }

  // Multistep processing : report progress.
  if ($context['sandbox']['progress'] != $context['sandbox']['max']) {
    $context['finished'] = $context['sandbox']['progress'] / $context['sandbox']['max'];
  }
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
