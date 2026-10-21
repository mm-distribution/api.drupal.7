# openid_menu_site_status_alter()

- **Type:** Function
- **File:** [`modules/openid/openid.module`](_file.md), lines 42–47 · [local source](../../../../source/modules/openid/openid.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module#L42-L47)
- **Module/theme:** openid
- **Implements:** [hook_menu_site_status_alter()](../../system/system.api.php/hook_menu_site_status_alter.md)

## Signature

```php
function openid_menu_site_status_alter(&$menu_site_status, $path)
```

## Documentation

```text
Implements hook_menu_site_status_alter().
```

## Code

```php
function openid_menu_site_status_alter(&$menu_site_status, $path) {
  // Allow access to openid/authenticate even if site is in offline mode.
  if ($menu_site_status == MENU_SITE_OFFLINE && user_is_anonymous() && $path == 'openid/authenticate') {
    $menu_site_status = MENU_SITE_ONLINE;
  }
}
```

---
_Drupal 7.103 · [modules/openid/openid.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module) · Licensed GPL-2.0-or-later (see LICENSE)._
