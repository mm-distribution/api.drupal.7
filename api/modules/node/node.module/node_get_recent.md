# node_get_recent()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 2312–2341 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L2312-L2341)
- **Module/theme:** node

## Signature

```php
function node_get_recent($number = 10)
```

## Documentation

```text
Finds the most recently changed nodes that are available to the current user.

@param $number
  (optional) The maximum number of nodes to find. Defaults to 10.

@return
  An array of node entities or an empty array if there are no recent nodes
  visible to the current user.
```

## Code

```php
function node_get_recent($number = 10) {
  $query = db_select('node', 'n');

  if (!user_access('bypass node access')) {
    // If the user is able to view their own unpublished nodes, allow them to
    // see these in addition to published nodes. Check that they actually have
    // some unpublished nodes to view before adding the condition.
    if (user_access('view own unpublished content') && $own_unpublished = db_query('SELECT nid FROM {node} WHERE uid = :uid AND status = :status', array(':uid' => $GLOBALS['user']->uid, ':status' => NODE_NOT_PUBLISHED))->fetchCol()) {
      $query->condition(db_or()
        ->condition('n.status', NODE_PUBLISHED)
        ->condition('n.nid', $own_unpublished, 'IN')
      );
    }
    else {
      // If not, restrict the query to published nodes.
      $query->condition('n.status', NODE_PUBLISHED);
    }
  }
  $nids = $query
    ->fields('n', array('nid'))
    ->orderBy('n.changed', 'DESC')
    ->range(0, $number)
    ->addTag('node_access')
    ->execute()
    ->fetchCol();

  $nodes = node_load_multiple($nids);

  return $nodes ? $nodes : array();
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
