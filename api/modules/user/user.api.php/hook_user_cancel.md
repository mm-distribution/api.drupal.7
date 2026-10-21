# hook_user_cancel()

- **Type:** Hook (documentation function)
- **File:** [`modules/user/user.api.php`](_file.md), lines 78–111 · [local source](../../../../source/modules/user/user.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.api.php#L78-L111)
- **Module/theme:** user
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_user_cancel($edit, $account, $method)
```

## Documentation

```text
Act on user account cancellations.

This hook is invoked from user_cancel() before a user account is canceled.
Depending on the account cancellation method, the module should either do
nothing, unpublish content, or anonymize content. See user_cancel_methods()
for the list of default account cancellation methods provided by User module.
Modules may add further methods via hook_user_cancel_methods_alter().

This hook is NOT invoked for the 'user_cancel_delete' account cancellation
method. To react on this method, implement hook_user_delete() instead.

Expensive operations should be added to the global account cancellation batch
by using batch_set().

@param $edit
  The array of form values submitted by the user.
@param $account
  The user object on which the operation is being performed.
@param $method
  The account cancellation method.

@see user_cancel_methods()
@see hook_user_cancel_methods_alter()
```

## Code

```php
function hook_user_cancel($edit, $account, $method) {
  switch ($method) {
    case 'user_cancel_block_unpublish':
      // Unpublish nodes (current revisions).
      module_load_include('inc', 'node', 'node.admin');
      $nodes = db_select('node', 'n')
        ->fields('n', array('nid'))
        ->condition('uid', $account->uid)
        ->execute()
        ->fetchCol();
      node_mass_update($nodes, array('status' => 0));
      break;

    case 'user_cancel_reassign':
      // Anonymize nodes (current revisions).
      module_load_include('inc', 'node', 'node.admin');
      $nodes = db_select('node', 'n')
        ->fields('n', array('nid'))
        ->condition('uid', $account->uid)
        ->execute()
        ->fetchCol();
      node_mass_update($nodes, array('uid' => 0));
      // Anonymize old revisions.
      db_update('node_revision')
        ->fields(array('uid' => 0))
        ->condition('uid', $account->uid)
        ->execute();
      // Clean history.
      db_delete('history')
        ->condition('uid', $account->uid)
        ->execute();
      break;
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_user_cancel()".

- [comment_user_cancel()](../../comment/comment.module/comment_user_cancel.md) — `modules/comment/comment.module`
- [node_user_cancel()](../../node/node.module/node_user_cancel.md) — `modules/node/node.module`
- [poll_user_cancel()](../../poll/poll.module/poll_user_cancel.md) — `modules/poll/poll.module`
- [profile_user_cancel()](../../profile/profile.module/profile_user_cancel.md) — `modules/profile/profile.module`
- [statistics_user_cancel()](../../statistics/statistics.module/statistics_user_cancel.md) — `modules/statistics/statistics.module`
- [trigger_user_cancel()](../../trigger/trigger.module/trigger_user_cancel.md) — `modules/trigger/trigger.module`

---
_Drupal 7.103 · [modules/user/user.api.php](https://github.com/drupal/drupal/blob/7.103/modules/user/user.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
