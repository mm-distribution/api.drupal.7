# user_cookie_delete()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 4114–4116 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L4114-L4116)
- **Module/theme:** user

## Signature

```php
function user_cookie_delete($cookie_name)
```

## Documentation

```text
Delete a visitor information cookie.

@param $cookie_name
  A cookie name such as 'homepage'.
```

## Code

```php
function user_cookie_delete($cookie_name) {
  setrawcookie('Drupal.visitor.' . $cookie_name, '', REQUEST_TIME - 3600, '/');
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
