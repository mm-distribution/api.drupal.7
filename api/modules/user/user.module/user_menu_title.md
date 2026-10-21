# user_menu_title()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 2055–2057 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L2055-L2057)
- **Module/theme:** user

## Signature

```php
function user_menu_title()
```

## Documentation

```text
Menu item title callback for the 'user' path.

Anonymous users should see "User account", but authenticated users are
expected to see "My account".
```

## Code

```php
function user_menu_title() {
  return user_is_logged_in() ? t('My account') : t('User account');
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
