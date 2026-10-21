# user_login_default_validators()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 2164–2166 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L2164-L2166)
- **Module/theme:** user

## Signature

```php
function user_login_default_validators()
```

## Documentation

```text
Set up a series for validators which check for blocked users,
then authenticate against local database, then return an error if
authentication fails. Distributed authentication modules are welcome
to use hook_form_alter() to change this series in order to
authenticate against their user database instead of the local users
table. If a distributed authentication module is successful, it
should set $form_state['uid'] to a user ID.

We use three validators instead of one since external authentication
modules usually only need to alter the second validator.

@see user_login_name_validate()
@see user_login_authenticate_validate()
@see user_login_final_validate()
@return array
  A simple list of validate functions.
```

## Code

```php
function user_login_default_validators() {
  return array('user_login_name_validate', 'user_login_authenticate_validate', 'user_login_final_validate');
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
