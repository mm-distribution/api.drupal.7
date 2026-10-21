# openid_user_logout()

- **Type:** Function
- **File:** [`modules/openid/openid.module`](_file.md), lines 116–120 · [local source](../../../../source/modules/openid/openid.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module#L116-L120)
- **Module/theme:** openid
- **Implements:** [hook_user_logout()](../../user/user.api.php/hook_user_logout.md)

## Signature

```php
function openid_user_logout($account)
```

## Documentation

```text
Implements hook_user_logout().

Delete any openid_identifier in visitor cookie.
```

## Code

```php
function openid_user_logout($account) {
  if (isset($_COOKIE['Drupal_visitor_openid_identifier'])) {
    user_cookie_delete('openid_identifier');
  }
}
```

---
_Drupal 7.103 · [modules/openid/openid.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module) · Licensed GPL-2.0-or-later (see LICENSE)._
