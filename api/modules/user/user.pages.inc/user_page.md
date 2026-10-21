# user_page()

- **Type:** Function
- **File:** [`modules/user/user.pages.inc`](_file.md), lines 698–707 · [local source](../../../../source/modules/user/user.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc#L698-L707)
- **Module/theme:** user

## Signature

```php
function user_page()
```

## Documentation

```text
Page callback: Displays the user page.

Displays user profile if user is logged in, or login form for anonymous
users.

@return
  A render array for either a user profile or a login form.

@see user_view_page()
@see user_login()
```

## Code

```php
function user_page() {
  global $user;
  if ($user->uid) {
    menu_set_active_item('user/' . $user->uid);
    return menu_execute_active_handler(NULL, FALSE);
  }
  else {
    return drupal_get_form('user_login');
  }
}
```

---
_Drupal 7.103 · [modules/user/user.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
