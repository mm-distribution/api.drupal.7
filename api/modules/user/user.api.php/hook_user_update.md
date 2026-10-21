# hook_user_update()

- **Type:** Hook (documentation function)
- **File:** [`modules/user/user.api.php`](_file.md), lines 293–300 · [local source](../../../../source/modules/user/user.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.api.php#L293-L300)
- **Module/theme:** user
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_user_update(&$edit, $account, $category)
```

## Documentation

```text
A user account was updated.

Modules may use this hook to update their user data in a custom storage
after a user account has been updated.

@param $edit
  The array of form values submitted by the user.
@param $account
  The user object on which the operation is performed.
@param $category
  The active category of user information being edited.

@see hook_user_presave()
@see hook_user_insert()
```

## Code

```php
function hook_user_update(&$edit, $account, $category) {
  db_insert('user_changes')
    ->fields(array(
      'uid' => $account->uid,
      'changed' => time(),
    ))
    ->execute();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_user_update()".

- [entity_crud_hook_test_user_update()](../../simpletest/tests/entity_crud_hook_test.module/entity_crud_hook_test_user_update.md) — `modules/simpletest/tests/entity_crud_hook_test.module`
- [trigger_user_update()](../../trigger/trigger.module/trigger_user_update.md) — `modules/trigger/trigger.module`

---
_Drupal 7.103 · [modules/user/user.api.php](https://github.com/drupal/drupal/blob/7.103/modules/user/user.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
