# node_node_access()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 3109–3131 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L3109-L3131)
- **Module/theme:** node
- **Topics:** [node_access](../../../topics/node_access.md)
- **Implements:** [hook_node_access()](../node.api.php/hook_node_access.md)

## Signature

```php
function node_node_access($node, $op, $account)
```

## Documentation

```text
Implements hook_node_access().
```

## Code

```php
function node_node_access($node, $op, $account) {
  $type = is_string($node) ? $node : $node->type;

  if (in_array($type, node_permissions_get_configured_types())) {
    if ($op == 'create' && user_access('create ' . $type . ' content', $account)) {
      return NODE_ACCESS_ALLOW;
    }

    if ($op == 'update') {
      if (user_access('edit any ' . $type . ' content', $account) || (user_access('edit own ' . $type . ' content', $account) && ($account->uid == $node->uid))) {
        return NODE_ACCESS_ALLOW;
      }
    }

    if ($op == 'delete') {
      if (user_access('delete any ' . $type . ' content', $account) || (user_access('delete own ' . $type . ' content', $account) && ($account->uid == $node->uid))) {
        return NODE_ACCESS_ALLOW;
      }
    }
  }

  return NODE_ACCESS_IGNORE;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
