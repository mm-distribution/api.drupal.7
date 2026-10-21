# hook_user_insert()

- **Type:** Hook (documentation function)
- **File:** [`modules/user/user.api.php`](_file.md), lines 268–275 · [local source](../../../../source/modules/user/user.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.api.php#L268-L275)
- **Module/theme:** user
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_user_insert(&$edit, $account, $category)
```

## Documentation

```text
A user account was created.

The module should save its custom additions to the user object into the
database.

@param $edit
  The array of form values submitted by the user.
@param $account
  The user object on which the operation is being performed.
@param $category
  The active category of user information being edited.

@see hook_user_presave()
@see hook_user_update()
```

## Code

```php
function hook_user_insert(&$edit, $account, $category) {
  db_insert('mytable')
    ->fields(array(
      'myfield' => $edit['myfield'],
      'uid' => $account->uid,
    ))
    ->execute();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_user_insert()".

- [entity_crud_hook_test_user_insert()](../../simpletest/tests/entity_crud_hook_test.module/entity_crud_hook_test_user_insert.md) — `modules/simpletest/tests/entity_crud_hook_test.module`
- [openid_user_insert()](../../openid/openid.module/openid_user_insert.md) — `modules/openid/openid.module`
- [profile_user_insert()](../../profile/profile.module/profile_user_insert.md) — `modules/profile/profile.module`
- [trigger_user_insert()](../../trigger/trigger.module/trigger_user_insert.md) — `modules/trigger/trigger.module`

---
_Drupal 7.103 · [modules/user/user.api.php](https://github.com/drupal/drupal/blob/7.103/modules/user/user.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
