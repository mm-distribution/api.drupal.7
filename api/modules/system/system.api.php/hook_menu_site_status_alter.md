# hook_menu_site_status_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 4750–4755 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L4750-L4755)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_menu_site_status_alter(&$menu_site_status, $path)
```

## Documentation

```text
Control site status before menu dispatching.

The hook is called after checking whether the site is offline but before
the current router item is retrieved and executed by
menu_execute_active_handler(). If the site is in offline mode,
$menu_site_status is set to MENU_SITE_OFFLINE.

@param $menu_site_status
  Supported values are MENU_SITE_OFFLINE, MENU_ACCESS_DENIED,
  MENU_NOT_FOUND and MENU_SITE_ONLINE. Any other value than
  MENU_SITE_ONLINE will skip the default menu handling system and be passed
  for delivery to drupal_deliver_page() with a NULL
  $default_delivery_callback.
@param $path
  Contains the system path that is going to be loaded. This is read only,
  use hook_url_inbound_alter() to change the path.
```

## Code

```php
function hook_menu_site_status_alter(&$menu_site_status, $path) {
  // Allow access to my_module/authentication even if site is in offline mode.
  if ($menu_site_status == MENU_SITE_OFFLINE && user_is_anonymous() && $path == 'my_module/authentication') {
    $menu_site_status = MENU_SITE_ONLINE;
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_menu_site_status_alter()".

- [menu_test_menu_site_status_alter()](../../simpletest/tests/menu_test.module/menu_test_menu_site_status_alter.md) — `modules/simpletest/tests/menu_test.module`
- [openid_menu_site_status_alter()](../../openid/openid.module/openid_menu_site_status_alter.md) — `modules/openid/openid.module`
- [openid_test_menu_site_status_alter()](../../openid/tests/openid_test.module/openid_test_menu_site_status_alter.md) — `modules/openid/tests/openid_test.module`
- [user_menu_site_status_alter()](../../user/user.module/user_menu_site_status_alter.md) — `modules/user/user.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
