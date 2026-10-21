# user_is_logged_in()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 1589–1591 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L1589-L1591)
- **Module/theme:** user

## Signature

```php
function user_is_logged_in()
```

## Documentation

```text
Determines if the current user is logged in.

@return bool
  TRUE if the user is logged in, FALSE if the user is anonymous.
```

## Code

```php
function user_is_logged_in() {
  return (bool) $GLOBALS['user']->uid;
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
