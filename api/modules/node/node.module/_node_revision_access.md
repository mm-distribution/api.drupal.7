# _node_revision_access()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 1897–1947 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L1897-L1947)
- **Module/theme:** node

## Signature

```php
function _node_revision_access($node, $op = 'view', $account = NULL)
```

## Documentation

```text
Access callback: Checks node revision access.

@param $node
  The node to check.
@param $op
  (optional) The specific operation being checked. Defaults to 'view.'
@param object $account
  (optional) A user object representing the user for whom the operation is
  to be performed. Determines access for a user other than the current user.

@return
  TRUE if the operation may be performed, FALSE otherwise.

@see node_menu()
```

## Code

```php
function _node_revision_access($node, $op = 'view', $account = NULL) {
  $access = &drupal_static(__FUNCTION__, array());

  $map = array(
    'view' => 'view revisions',
    'update' => 'revert revisions',
    'delete' => 'delete revisions',
  );

  if (!$node || !isset($map[$op])) {
    // If there was no node to check against, or the $op was not one of the
    // supported ones, we return access denied.
    return FALSE;
  }

  if (!isset($account)) {
    $account = $GLOBALS['user'];
  }

  // Statically cache access by revision ID, user account ID, and operation.
  $cid = $node->vid . ':' . $account->uid . ':' . $op;

  if (!isset($access[$cid])) {
    // Perform basic permission checks first.
    if (!user_access($map[$op], $account) && !user_access('administer nodes', $account)) {
      return $access[$cid] = FALSE;
    }

    $node_current_revision = node_load($node->nid);
    $is_current_revision = $node_current_revision->vid == $node->vid;

    // There should be at least two revisions. If the vid of the given node and
    // the vid of the current revision differ, then we already have two
    // different revisions so there is no need for a separate database check.
    // Also, if you try to revert to or delete the current revision, that's not
    // good.
    if ($is_current_revision && (db_query('SELECT COUNT(vid) FROM {node_revision} WHERE nid = :nid', array(':nid' => $node->nid))->fetchField() == 1 || $op == 'update' || $op == 'delete')) {
      $access[$cid] = FALSE;
    }
    elseif (user_access('administer nodes', $account)) {
      $access[$cid] = TRUE;
    }
    else {
      // First check the access to the current revision and finally, if the node
      // passed in is not the current revision then access to that, too.
      $access[$cid] = node_access($op, $node_current_revision, $account) && ($is_current_revision || node_access($op, $node, $account));
    }
  }

  return $access[$cid];
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
