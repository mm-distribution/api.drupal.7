# hook_user_delete()

- **Type:** Hook (documentation function)
- **File:** [`modules/user/user.api.php`](_file.md), lines 47–51 · [local source](../../../../source/modules/user/user.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.api.php#L47-L51)
- **Module/theme:** user
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_user_delete($account)
```

## Documentation

```text
Respond to user deletion.

This hook is invoked from user_delete_multiple() before field_attach_delete()
is called and before users are actually removed from the database.

Modules should additionally implement hook_user_cancel() to process stored
user data for other account cancellation methods.

@param $account
  The account that is being deleted.

@see user_delete_multiple()
```

## Code

```php
function hook_user_delete($account) {
  db_delete('mytable')
    ->condition('uid', $account->uid)
    ->execute();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_user_delete()".

- [entity_crud_hook_test_user_delete()](../../simpletest/tests/entity_crud_hook_test.module/entity_crud_hook_test_user_delete.md) — `modules/simpletest/tests/entity_crud_hook_test.module`
- [comment_user_delete()](../../comment/comment.module/comment_user_delete.md) — `modules/comment/comment.module`
- [node_user_delete()](../../node/node.module/node_user_delete.md) — `modules/node/node.module`
- [poll_user_delete()](../../poll/poll.module/poll_user_delete.md) — `modules/poll/poll.module`
- [profile_user_delete()](../../profile/profile.module/profile_user_delete.md) — `modules/profile/profile.module`
- [statistics_user_delete()](../../statistics/statistics.module/statistics_user_delete.md) — `modules/statistics/statistics.module`
- [trigger_user_delete()](../../trigger/trigger.module/trigger_user_delete.md) — `modules/trigger/trigger.module`

---
_Drupal 7.103 · [modules/user/user.api.php](https://github.com/drupal/drupal/blob/7.103/modules/user/user.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
