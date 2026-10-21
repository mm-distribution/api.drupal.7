# user_login_submit()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 2350–2356 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L2350-L2356)
- **Module/theme:** user

## Signature

```php
function user_login_submit($form, &$form_state)
```

## Documentation

```text
Submit handler for the login form. Load $user object and perform standard login
tasks. The user is then redirected to the My Account page. Setting the
destination in the query string overrides the redirect.
```

## Code

```php
function user_login_submit($form, &$form_state) {
  global $user;
  $user = user_load($form_state['uid']);
  $form_state['redirect'] = 'user/' . $user->uid;

  user_login_finalize($form_state);
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
