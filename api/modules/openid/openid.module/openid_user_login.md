# openid_user_login()

- **Type:** Function
- **File:** [`modules/openid/openid.module`](_file.md), lines 103–109 · [local source](../../../../source/modules/openid/openid.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module#L103-L109)
- **Module/theme:** openid
- **Implements:** [hook_user_login()](../../user/user.api.php/hook_user_login.md)

## Signature

```php
function openid_user_login(&$edit, $account)
```

## Documentation

```text
Implements hook_user_login().

Save openid_identifier to visitor cookie.
```

## Code

```php
function openid_user_login(&$edit, $account) {
  if (isset($_SESSION['openid'])) {
    // The user has logged in via OpenID.
    user_cookie_save(array_intersect_key($_SESSION['openid']['user_login_values'], array_flip(array('openid_identifier'))));
    unset($_SESSION['openid']);
  }
}
```

---
_Drupal 7.103 · [modules/openid/openid.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module) · Licensed GPL-2.0-or-later (see LICENSE)._
