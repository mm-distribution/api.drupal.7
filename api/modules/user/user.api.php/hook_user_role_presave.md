# hook_user_role_presave()

- **Type:** Hook (documentation function)
- **File:** [`modules/user/user.api.php`](_file.md), lines 408–413 · [local source](../../../../source/modules/user/user.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.api.php#L408-L413)
- **Module/theme:** user
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_user_role_presave($role)
```

## Documentation

```text
Act on a user role being inserted or updated.

Modules implementing this hook can act on the user role object before
it has been saved to the database.

@param $role
  A user role object.

@see hook_user_role_insert()
@see hook_user_role_update()
```

## Code

```php
function hook_user_role_presave($role) {
  // Set a UUID for the user role if it doesn't already exist
  if (empty($role->uuid)) {
    $role->uuid = uuid_uuid();
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_user_role_presave()".

_None found._

---
_Drupal 7.103 · [modules/user/user.api.php](https://github.com/drupal/drupal/blob/7.103/modules/user/user.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
