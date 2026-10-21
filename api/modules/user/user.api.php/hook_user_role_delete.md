# hook_user_role_delete()

- **Type:** Hook (documentation function)
- **File:** [`modules/user/user.api.php`](_file.md), lines 468–473 · [local source](../../../../source/modules/user/user.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.api.php#L468-L473)
- **Module/theme:** user
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_user_role_delete($role)
```

## Documentation

```text
Respond to user role deletion.

This hook allows you act when a user role has been deleted.
If your module stores references to roles, it's recommended that you
implement this hook and delete existing instances of the deleted role
in your module database tables.

@param $role
  The $role object being deleted.
```

## Code

```php
function hook_user_role_delete($role) {
  // Delete existing instances of the deleted role.
  db_delete('my_module_table')
    ->condition('rid', $role->rid)
    ->execute();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_user_role_delete()".

- [block_user_role_delete()](../../block/block.module/block_user_role_delete.md) — `modules/block/block.module`

---
_Drupal 7.103 · [modules/user/user.api.php](https://github.com/drupal/drupal/blob/7.103/modules/user/user.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
