# node_access_view_all_nodes()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 3251–3285 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L3251-L3285)
- **Module/theme:** node
- **Topics:** [node_access](../../../topics/node_access.md)

## Signature

```php
function node_access_view_all_nodes($account = NULL)
```

## Documentation

```text
Determines whether the user has a global viewing grant for all nodes.

Checks to see whether any module grants global 'view' access to a user
account; global 'view' access is encoded in the {node_access} table as a
grant with nid=0. If no node access modules are enabled, node.module defines
such a global 'view' access grant.

This function is called when a node listing query is tagged with
'node_access'; when this function returns TRUE, no node access joins are
added to the query.

@param $account
  The user object for the user whose access is being checked. If omitted,
  the current user is used.

@return
  TRUE if 'view' access to all nodes is granted, FALSE otherwise.

@see hook_node_grants()
@see _node_query_node_access_alter()
```

## Code

```php
function node_access_view_all_nodes($account = NULL) {
  global $user;
  if (!$account) {
    $account = $user;
  }

  // Statically cache results in an array keyed by $account->uid.
  $access = &drupal_static(__FUNCTION__);
  if (isset($access[$account->uid])) {
    return $access[$account->uid];
  }

  // If no modules implement the node access system, access is always TRUE.
  if (!module_implements('node_grants')) {
    $access[$account->uid] = TRUE;
  }
  else {
    $query = db_select('node_access');
    $query->addExpression('COUNT(*)');
    $query
      ->condition('nid', 0)
      ->condition('grant_view', 1, '>=');

    $grants = node_add_node_grants_to_query(node_access_grants('view', $account));

    if (count($grants) > 0 ) {
      $query->condition($grants);
    }
    $access[$account->uid] = $query
      ->execute()
      ->fetchField();
  }

  return $access[$account->uid];
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
