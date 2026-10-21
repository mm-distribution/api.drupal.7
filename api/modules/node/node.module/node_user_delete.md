# node_user_delete()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 1832–1850 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L1832-L1850)
- **Module/theme:** node
- **Implements:** [hook_user_delete()](../../user/user.api.php/hook_user_delete.md)

## Signature

```php
function node_user_delete($account)
```

## Documentation

```text
Implements hook_user_delete().
```

## Code

```php
function node_user_delete($account) {
  // Delete nodes (current revisions).
  // @todo Introduce node_mass_delete() or make node_mass_update() more flexible.
  $nodes = db_select('node', 'n')
    ->fields('n', array('nid'))
    ->condition('uid', $account->uid)
    ->execute()
    ->fetchCol();
  node_delete_multiple($nodes);
  // Delete old revisions.
  $revisions = db_query('SELECT vid FROM {node_revision} WHERE uid = :uid', array(':uid' => $account->uid))->fetchCol();
  foreach ($revisions as $revision) {
    node_revision_delete($revision);
  }
  // Clean history.
  db_delete('history')
    ->condition('uid', $account->uid)
    ->execute();
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
