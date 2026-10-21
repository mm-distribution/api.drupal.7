# user_page_title()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 2062–2064 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L2062-L2064)
- **Module/theme:** user

## Signature

```php
function user_page_title($account)
```

## Documentation

```text
Menu item title callback - use the user name.
```

## Code

```php
function user_page_title($account) {
  return is_object($account) ? format_username($account) : '';
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
