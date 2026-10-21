# user_delete_multiple()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 2623–2653 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L2623-L2653)
- **Module/theme:** user

## Signature

```php
function user_delete_multiple(array $uids)
```

## Documentation

```text
Delete multiple user accounts.

@param $uids
  An array of user IDs.
```

## Code

```php
function user_delete_multiple(array $uids) {
  if (!empty($uids)) {
    $accounts = user_load_multiple($uids, array());

    $transaction = db_transaction();
    try {
      foreach ($accounts as $uid => $account) {
        module_invoke_all('user_delete', $account);
        module_invoke_all('entity_delete', $account, 'user');
        field_attach_delete('user', $account);
        drupal_session_destroy_uid($account->uid);
      }

      db_delete('users')
        ->condition('uid', $uids, 'IN')
        ->execute();
      db_delete('users_roles')
        ->condition('uid', $uids, 'IN')
        ->execute();
      db_delete('authmap')
        ->condition('uid', $uids, 'IN')
        ->execute();
    }
    catch (Exception $e) {
      $transaction->rollback();
      watchdog_exception('user', $e);
      throw $e;
    }
    entity_get_controller('user')->resetCache();
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
