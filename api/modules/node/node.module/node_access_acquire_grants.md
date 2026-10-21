# node_access_acquire_grants()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 3496–3515 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L3496-L3515)
- **Module/theme:** node
- **Topics:** [node_access](../../../topics/node_access.md)

## Signature

```php
function node_access_acquire_grants($node, $delete = TRUE)
```

## Documentation

```text
Gets the list of node access grants and writes them to the database.

This function is called when a node is saved, and can also be called by
modules if something other than a node save causes node access permissions to
change. It collects all node access grants for the node from
hook_node_access_records() implementations, allows these grants to be altered
via hook_node_access_records_alter() implementations, and saves the collected
and altered grants to the database.

@param $node
  The $node to acquire grants for.

@param $delete
  Whether to delete existing node access records before inserting new ones.
  Defaults to TRUE.
```

## Code

```php
function node_access_acquire_grants($node, $delete = TRUE) {
  $grants = module_invoke_all('node_access_records', $node);
  // Let modules alter the grants.
  drupal_alter('node_access_records', $grants, $node);
  // If no grants are set and the node is published, then use the default grant.
  if (empty($grants) && !empty($node->status)) {
    $grants[] = array('realm' => 'all', 'gid' => 0, 'grant_view' => 1, 'grant_update' => 0, 'grant_delete' => 0);
  }
  else {
    // Retain grants by highest priority.
    $grant_by_priority = array();
    foreach ($grants as $g) {
      $grant_by_priority[intval($g['priority'])][] = $g;
    }
    krsort($grant_by_priority);
    $grants = array_shift($grant_by_priority);
  }

  node_access_write_grants($node, $grants, NULL, $delete);
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
