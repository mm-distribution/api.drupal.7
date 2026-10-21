# user_uid_only_optional_to_arg()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 1975–1977 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L1975-L1977)
- **Module/theme:** user

## Signature

```php
function user_uid_only_optional_to_arg($arg)
```

## Documentation

```text
Returns $arg or the user ID of the current user if $arg is '%' or empty.

Deprecated. Use %user_uid_optional instead.

@todo D8: Remove.
```

## Code

```php
function user_uid_only_optional_to_arg($arg) {
  return user_uid_optional_to_arg($arg);
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
