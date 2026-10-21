# hook_user_presave()

- **Type:** Hook (documentation function)
- **File:** [`modules/user/user.api.php`](_file.md), lines 244–250 · [local source](../../../../source/modules/user/user.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.api.php#L244-L250)
- **Module/theme:** user
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_user_presave(&$edit, $account, $category)
```

## Documentation

```text
A user account is about to be created or updated.

This hook is primarily intended for modules that want to store properties in
the serialized {users}.data column, which is automatically loaded whenever a
user account object is loaded, modules may add to $edit['data'] in order
to have their data serialized on save.

@param $edit
  The array of form values submitted by the user. Assign values to this
  array to save changes in the database.
@param $account
  The user object on which the operation is performed. Values assigned in
  this object will not be saved in the database.
@param $category
  The active category of user information being edited.

@see hook_user_insert()
@see hook_user_update()
```

## Code

```php
function hook_user_presave(&$edit, $account, $category) {
  // Make sure that our form value 'mymodule_foo' is stored as
  // 'mymodule_bar' in the 'data' (serialized) column.
  if (isset($edit['mymodule_foo'])) {
    $edit['data']['mymodule_bar'] = $edit['mymodule_foo'];
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_user_presave()".

- [entity_crud_hook_test_user_presave()](../../simpletest/tests/entity_crud_hook_test.module/entity_crud_hook_test_user_presave.md) — `modules/simpletest/tests/entity_crud_hook_test.module`
- [block_user_presave()](../../block/block.module/block_user_presave.md) — `modules/block/block.module`
- [contact_user_presave()](../../contact/contact.module/contact_user_presave.md) — `modules/contact/contact.module`
- [overlay_user_presave()](../../overlay/overlay.module/overlay_user_presave.md) — `modules/overlay/overlay.module`
- [profile_user_presave()](../../profile/profile.module/profile_user_presave.md) — `modules/profile/profile.module`
- [user_user_presave()](../user.module/user_user_presave.md) — `modules/user/user.module`

---
_Drupal 7.103 · [modules/user/user.api.php](https://github.com/drupal/drupal/blob/7.103/modules/user/user.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
