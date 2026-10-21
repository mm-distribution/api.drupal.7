# user_logout()

- **Type:** Function
- **File:** [`modules/user/user.pages.inc`](_file.md), lines 303–306 · [local source](../../../../source/modules/user/user.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc#L303-L306)
- **Module/theme:** user

## Signature

```php
function user_logout()
```

## Documentation

```text
Menu callback; logs the current user out, and redirects to the home page.
```

## Code

```php
function user_logout() {
  user_logout_current_user();
  drupal_goto();
}
```

---
_Drupal 7.103 · [modules/user/user.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
