# user_is_anonymous()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 1578–1581 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L1578-L1581)
- **Module/theme:** user

## Signature

```php
function user_is_anonymous()
```

## Documentation

```text
Determines if the current user is anonymous.

@return bool
  TRUE if the user is anonymous, FALSE if the user is authenticated.
```

## Code

```php
function user_is_anonymous() {
  // Menu administrators can see items for anonymous when administering.
  return !$GLOBALS['user']->uid || !empty($GLOBALS['menu_admin']);
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
