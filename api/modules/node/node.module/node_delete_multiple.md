# node_delete_multiple()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 1244–1289 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L1244-L1289)
- **Module/theme:** node

## Signature

```php
function node_delete_multiple($nids)
```

## Documentation

```text
Deletes multiple nodes.

@param $nids
  An array of node IDs.
```

## Code

```php
function node_delete_multiple($nids) {
  $transaction = db_transaction();
  if (!empty($nids)) {
    $nodes = node_load_multiple($nids, array());

    try {
      foreach ($nodes as $nid => $node) {
        // Call the node-specific callback (if any):
        node_invoke($node, 'delete');
        module_invoke_all('node_delete', $node);
        module_invoke_all('entity_delete', $node, 'node');
        field_attach_delete('node', $node);

        // Remove this node from the search index if needed.
        // This code is implemented in node module rather than in search module,
        // because node module is implementing search module's API, not the other
        // way around.
        if (module_exists('search')) {
          search_reindex($nid, 'node');
        }
      }

      // Delete after calling hooks so that they can query node tables as needed.
      db_delete('node')
        ->condition('nid', $nids, 'IN')
        ->execute();
      db_delete('node_revision')
        ->condition('nid', $nids, 'IN')
        ->execute();
      db_delete('history')
        ->condition('nid', $nids, 'IN')
        ->execute();
      db_delete('node_access')
       ->condition('nid', $nids, 'IN')
       ->execute();
    }
    catch (Exception $e) {
      $transaction->rollback();
      watchdog_exception('node', $e);
      throw $e;
    }

    // Clear the page and block and node_load_multiple caches.
    entity_get_controller('node')->resetCache();
  }
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
