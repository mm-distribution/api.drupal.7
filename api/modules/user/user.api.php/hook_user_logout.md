# hook_user_logout()

- **Type:** Hook (documentation function)
- **File:** [`modules/user/user.api.php`](_file.md), lines 331–338 · [local source](../../../../source/modules/user/user.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.api.php#L331-L338)
- **Module/theme:** user
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_user_logout($account)
```

## Documentation

```text
The user just logged out.

Note that when this hook is invoked, the changes have not yet been written to
the database, because a database transaction is still in progress. The
transaction is not finalized until the save operation is entirely completed
and user_save() goes out of scope. You should not rely on data in the
database at this time as it is not updated yet. You should also note that any
write/update database queries executed from this hook are also not committed
immediately. Check user_save() and db_transaction() for more info.

@param $account
  The user object on which the operation was just performed.
```

## Code

```php
function hook_user_logout($account) {
  db_insert('logouts')
    ->fields(array(
      'uid' => $account->uid,
      'time' => time(),
    ))
    ->execute();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_user_logout()".

- [openid_user_logout()](../../openid/openid.module/openid_user_logout.md) — `modules/openid/openid.module`
- [trigger_user_logout()](../../trigger/trigger.module/trigger_user_logout.md) — `modules/trigger/trigger.module`

---
_Drupal 7.103 · [modules/user/user.api.php](https://github.com/drupal/drupal/blob/7.103/modules/user/user.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
