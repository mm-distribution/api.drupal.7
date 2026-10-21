# user_cookie_save()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 4101–4106 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L4101-L4106)
- **Module/theme:** user

## Signature

```php
function user_cookie_save(array $values)
```

## Documentation

```text
Saves visitor information as a cookie so it can be reused.

@param $values
  An array of key/value pairs to be saved into a cookie.
```

## Code

```php
function user_cookie_save(array $values) {
  foreach ($values as $field => $value) {
    // Set cookie for 365 days.
    setrawcookie('Drupal.visitor.' . $field, rawurlencode($value), REQUEST_TIME + 31536000, '/');
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
