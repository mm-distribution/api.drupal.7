# user_menu_site_status_alter()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 1888–1925 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L1888-L1925)
- **Module/theme:** user
- **Implements:** [hook_menu_site_status_alter()](../../system/system.api.php/hook_menu_site_status_alter.md)

## Signature

```php
function user_menu_site_status_alter(&$menu_site_status, $path)
```

## Documentation

```text
Implements hook_menu_site_status_alter().
```

## Code

```php
function user_menu_site_status_alter(&$menu_site_status, $path) {
  if ($menu_site_status == MENU_SITE_OFFLINE) {
    // If the site is offline, log out unprivileged users.
    if (user_is_logged_in() && !user_access('access site in maintenance mode')) {
      module_load_include('pages.inc', 'user', 'user');
      user_logout();
    }

    if (user_is_anonymous()) {
      switch ($path) {
        case 'user':
          // Forward anonymous user to login page.
          drupal_goto('user/login');
        case 'user/login':
        case 'user/password':
          // Disable offline mode.
          $menu_site_status = MENU_SITE_ONLINE;
          break;
        default:
          if (strpos($path, 'user/reset/') === 0) {
            // Disable offline mode.
            $menu_site_status = MENU_SITE_ONLINE;
          }
          break;
      }
    }
  }
  if (user_is_logged_in()) {
    if ($path == 'user/login') {
      // If user is logged in, redirect to 'user' instead of giving 403.
      drupal_goto('user');
    }
    if ($path == 'user/register') {
      // Authenticated user should be redirected to user edit page.
      drupal_goto('user/' . $GLOBALS['user']->uid . '/edit');
    }
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
