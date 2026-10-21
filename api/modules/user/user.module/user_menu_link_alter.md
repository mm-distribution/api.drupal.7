# user_menu_link_alter()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 1930–1944 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L1930-L1944)
- **Module/theme:** user
- **Implements:** [hook_menu_link_alter()](../../system/system.api.php/hook_menu_link_alter.md)

## Signature

```php
function user_menu_link_alter(&$link)
```

## Documentation

```text
Implements hook_menu_link_alter().
```

## Code

```php
function user_menu_link_alter(&$link) {
  // The path 'user' must be accessible for anonymous users, but only visible
  // for authenticated users. Authenticated users should see "My account", but
  // anonymous users should not see it at all. Therefore, invoke
  // user_translated_menu_link_alter() to conditionally hide the link.
  if ($link['link_path'] == 'user' && isset($link['module']) && $link['module'] == 'system') {
    $link['options']['alter'] = TRUE;
  }

  // Force the Logout link to appear on the top-level of 'user-menu' menu by
  // default (i.e., unless it has been customized).
  if ($link['link_path'] == 'user/logout' && isset($link['module']) && $link['module'] == 'system' && empty($link['customized'])) {
    $link['plid'] = 0;
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
