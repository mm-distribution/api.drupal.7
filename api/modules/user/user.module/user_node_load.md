# user_node_load()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 3728–3744 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L3728-L3744)
- **Module/theme:** user
- **Implements:** [hook_node_load()](../../node/node.api.php/hook_node_load.md)

## Signature

```php
function user_node_load($nodes, $types)
```

## Documentation

```text
Implements hook_node_load().
```

## Code

```php
function user_node_load($nodes, $types) {
  // Build an array of all uids for node authors, keyed by nid.
  $uids = array();
  foreach ($nodes as $nid => $node) {
    $uids[$nid] = $node->uid;
  }

  // Fetch name, picture, and data for these users.
  $user_fields = db_query("SELECT uid, name, picture, data FROM {users} WHERE uid IN (:uids)", array(':uids' => $uids))->fetchAllAssoc('uid');

  // Add these values back into the node objects.
  foreach ($uids as $nid => $uid) {
    $nodes[$nid]->name = $user_fields[$uid]->name;
    $nodes[$nid]->picture = $user_fields[$uid]->picture;
    $nodes[$nid]->data = $user_fields[$uid]->data;
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
