# user_view_page()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 2658–2662 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L2658-L2662)
- **Module/theme:** user

## Signature

```php
function user_view_page($account)
```

## Documentation

```text
Page callback wrapper for user_view().
```

## Code

```php
function user_view_page($account) {
  // An administrator may try to view a non-existent account,
  // so we give them a 404 (versus a 403 for non-admins).
  return is_object($account) ? user_view($account) : MENU_NOT_FOUND;
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
