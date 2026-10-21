# hook_user_load()

- **Type:** Hook (documentation function)
- **File:** [`modules/user/user.api.php`](_file.md), lines 26–31 · [local source](../../../../source/modules/user/user.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.api.php#L26-L31)
- **Module/theme:** user
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_user_load($users)
```

## Documentation

```text
Act on user objects when loaded from the database.

Due to the static cache in user_load_multiple() you should not use this
hook to modify the user properties returned by the {users} table itself
since this may result in unreliable results when loading from cache.

@param $users
  An array of user objects, indexed by uid.

@see user_load_multiple()
@see profile_user_load()
```

## Code

```php
function hook_user_load($users) {
  $result = db_query('SELECT uid, foo FROM {my_table} WHERE uid IN (:uids)', array(':uids' => array_keys($users)));
  foreach ($result as $record) {
    $users[$record->uid]->foo = $record->foo;
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_user_load()".

- [entity_crud_hook_test_user_load()](../../simpletest/tests/entity_crud_hook_test.module/entity_crud_hook_test_user_load.md) — `modules/simpletest/tests/entity_crud_hook_test.module`
- [profile_user_load()](../../profile/profile.module/profile_user_load.md) — `modules/profile/profile.module`
- [anonymous_user_unblock_test_user_load()](../tests/anonymous_user_unblock_test.module/anonymous_user_unblock_test_user_load.md) — `modules/user/tests/anonymous_user_unblock_test.module`

---
_Drupal 7.103 · [modules/user/user.api.php](https://github.com/drupal/drupal/blob/7.103/modules/user/user.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
