# user_login_destination()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 4087–4093 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L4087-L4093)
- **Module/theme:** user

## Signature

```php
function user_login_destination()
```

## Documentation

```text
Helper function to rewrite the destination to avoid redirecting to login page after login.

Third-party authentication modules may use this function to determine the
proper destination after a user has been properly logged in.
```

## Code

```php
function user_login_destination() {
  $destination = drupal_get_destination();
  if ($destination['destination'] == 'user/login') {
    $destination['destination'] = 'user';
  }
  return $destination;
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
