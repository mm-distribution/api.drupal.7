# hook_user_role_update()

- **Type:** Hook (documentation function)
- **File:** [`modules/user/user.api.php`](_file.md), lines 447–455 · [local source](../../../../source/modules/user/user.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.api.php#L447-L455)
- **Module/theme:** user
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_user_role_update($role)
```

## Documentation

```text
Respond to updates to a user role.

Modules implementing this hook can act on the user role object when updated.
It's recommended that you implement this hook if your module adds additional
data to user roles object. The module should save its custom additions to
the database.

@param $role
  A user role object.
```

## Code

```php
function hook_user_role_update($role) {
  // Save extra fields provided by the module to user roles.
  db_merge('my_module_table')
    ->key(array('rid' => $role->rid))
    ->fields(array(
      'role_description' => $role->description
    ))
    ->execute();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_user_role_update()".

_None found._

---
_Drupal 7.103 · [modules/user/user.api.php](https://github.com/drupal/drupal/blob/7.103/modules/user/user.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
