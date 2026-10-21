# user_uid_optional_to_arg()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 2042–2047 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L2042-L2047)
- **Module/theme:** user

## Signature

```php
function user_uid_optional_to_arg($arg)
```

## Documentation

```text
Returns $arg or the user ID of the current user if $arg is '%' or empty.

@todo rethink the naming of this in Drupal 8.
```

## Code

```php
function user_uid_optional_to_arg($arg) {
  // Give back the current user uid when called from eg. tracker, aka.
  // with an empty arg. Also use the current user uid when called from
  // the menu with a % for the current account link.
  return empty($arg) || $arg == '%' ? $GLOBALS['user']->uid : $arg;
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
