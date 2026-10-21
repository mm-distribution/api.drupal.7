# node_access()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 2990–3079 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L2990-L3079)
- **Module/theme:** node
- **Topics:** [node_access](../../../topics/node_access.md)

## Signature

```php
function node_access($op, $node, $account = NULL)
```

## Documentation

```text
Determines whether the current user may perform the operation on the node.

@param $op
  The operation to be performed on the node. Possible values are:
  - "view"
  - "update"
  - "delete"
  - "create"
@param $node
  The node object on which the operation is to be performed, or node type
  (e.g. 'forum') for "create" operation.
@param $account
  Optional, a user object representing the user for whom the operation is to
  be performed. Determines access for a user other than the current user.

@return
  TRUE if the operation may be performed, FALSE otherwise.
```

## Code

```php
function node_access($op, $node, $account = NULL) {
  $rights = &drupal_static(__FUNCTION__, array());

  if (!$node || !in_array($op, array('view', 'update', 'delete', 'create'), TRUE)) {
    // If there was no node to check against, or the $op was not one of the
    // supported ones, we return access denied.
    return FALSE;
  }
  // If no user object is supplied, the access check is for the current user.
  if (empty($account)) {
    $account = $GLOBALS['user'];
  }

  // $node may be either an object or a node type. Since node types cannot be
  // an integer, use either nid or type as the static cache id.

  $cid = is_object($node) ? $node->nid : $node;

  // If we've already checked access for this node, user and op, return from
  // cache.
  if (isset($rights[$account->uid][$cid][$op])) {
    return $rights[$account->uid][$cid][$op];
  }

  if (user_access('bypass node access', $account)) {
    $rights[$account->uid][$cid][$op] = TRUE;
    return TRUE;
  }
  if (!user_access('access content', $account)) {
    $rights[$account->uid][$cid][$op] = FALSE;
    return FALSE;
  }

  // We grant access to the node if both of the following conditions are met:
  // - No modules say to deny access.
  // - At least one module says to grant access.
  // If no module specified either allow or deny, we fall back to the
  // node_access table.
  $access = module_invoke_all('node_access', $node, $op, $account);
  if (in_array(NODE_ACCESS_DENY, $access, TRUE)) {
    $rights[$account->uid][$cid][$op] = FALSE;
    return FALSE;
  }
  elseif (in_array(NODE_ACCESS_ALLOW, $access, TRUE)) {
    $rights[$account->uid][$cid][$op] = TRUE;
    return TRUE;
  }

  // Check if authors can view their own unpublished nodes.
  if ($op == 'view' && !$node->status && user_access('view own unpublished content', $account) && $account->uid == $node->uid && $account->uid != 0) {
    $rights[$account->uid][$cid][$op] = TRUE;
    return TRUE;
  }

  // If the module did not override the access rights, use those set in the
  // node_access table.
  if ($op != 'create' && $node->nid) {
    if (module_implements('node_grants')) {
      $query = db_select('node_access');
      $query->addExpression('1');
      $query->condition('grant_' . $op, 1, '>=');
      $nids = db_or()->condition('nid', $node->nid);
      if ($node->status) {
        $nids->condition('nid', 0);
      }
      $query->condition($nids);
      $query->range(0, 1);

      $grants = node_add_node_grants_to_query(node_access_grants($op, $account));

      if (count($grants) > 0) {
        $query->condition($grants);
      }

      $result =  (bool) $query
        ->execute()
        ->fetchField();
      $rights[$account->uid][$cid][$op] = $result;
      return $result;
    }
    elseif (is_object($node) && $op == 'view' && $node->status) {
      // If no modules implement hook_node_grants(), the default behavior is to
      // allow all users to view published nodes, so reflect that here.
      $rights[$account->uid][$cid][$op] = TRUE;
      return TRUE;
    }
  }

  return FALSE;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
