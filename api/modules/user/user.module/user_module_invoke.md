# user_module_invoke()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 98–103 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L98-L103)
- **Module/theme:** user

## Signature

```php
function user_module_invoke($type, &$edit, $account, $category = NULL)
```

## Documentation

```text
Invokes a user hook in every module.

We cannot use module_invoke() for this, because the arguments need to
be passed by reference.

@param $type
  A text string that controls which user hook to invoke.  Valid choices are:
  - cancel: Invokes hook_user_cancel().
  - insert: Invokes hook_user_insert().
  - login: Invokes hook_user_login().
  - presave: Invokes hook_user_presave().
  - update: Invokes hook_user_update().
@param $edit
  An associative array variable containing form values to be passed
  as the first parameter of the hook function.
@param $account
  The user account object to be passed as the second parameter of the hook
  function.
@param $category
  The category of user information being acted upon.
```

## Code

```php
function user_module_invoke($type, &$edit, $account, $category = NULL) {
  foreach (module_implements('user_' . $type) as $module) {
    $function = $module . '_user_' . $type;
    $function($edit, $account, $category);
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
