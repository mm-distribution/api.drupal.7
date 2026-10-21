# user_load()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 365–368 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L365-L368)
- **Module/theme:** user

## Signature

```php
function user_load($uid, $reset = FALSE)
```

## Documentation

```text
Loads a user object.

Drupal has a global $user object, which represents the currently-logged-in
user. So to avoid confusion and to avoid clobbering the global $user object,
it is a good idea to assign the result of this function to a different local
variable, generally $account. If you actually do want to act as the user you
are loading, it is essential to call drupal_save_session(FALSE); first.
See
@link http://drupal.org/node/218104 Safely impersonating another user @endlink
for more information.

@param $uid
  Integer specifying the user ID to load.
@param $reset
  TRUE to reset the internal cache and load from the database; FALSE
  (default) to load from the internal cache, if set.

@return
  A fully-loaded user object upon successful user load, or FALSE if the user
  cannot be loaded.

@see user_load_multiple()
```

## Code

```php
function user_load($uid, $reset = FALSE) {
  $users = user_load_multiple(array($uid), array(), $reset);
  return reset($users);
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
