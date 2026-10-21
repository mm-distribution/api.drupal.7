# user_translated_menu_link_alter()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 1949–1954 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L1949-L1954)
- **Module/theme:** user
- **Implements:** [hook_translated_menu_link_alter()](../../system/system.api.php/hook_translated_menu_link_alter.md)

## Signature

```php
function user_translated_menu_link_alter(&$link)
```

## Documentation

```text
Implements hook_translated_menu_link_alter().
```

## Code

```php
function user_translated_menu_link_alter(&$link) {
  // Hide the "User account" link for anonymous users.
  if ($link['link_path'] == 'user' && $link['module'] == 'system' && !$GLOBALS['user']->uid) {
    $link['hidden'] = 1;
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
