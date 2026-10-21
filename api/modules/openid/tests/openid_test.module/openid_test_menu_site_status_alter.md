# openid_test_menu_site_status_alter()

- **Type:** Function
- **File:** [`modules/openid/tests/openid_test.module`](_file.md), lines 82–87 · [local source](../../../../../source/modules/openid/tests/openid_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/tests/openid_test.module#L82-L87)
- **Module/theme:** openid_test
- **Implements:** [hook_menu_site_status_alter()](../../../system/system.api.php/hook_menu_site_status_alter.md)

## Signature

```php
function openid_test_menu_site_status_alter(&$menu_site_status, $path)
```

## Documentation

```text
Implements hook_menu_site_status_alter().
```

## Code

```php
function openid_test_menu_site_status_alter(&$menu_site_status, $path) {
  // Allow access to openid endpoint and identity even in offline mode.
  if ($menu_site_status == MENU_SITE_OFFLINE && user_is_anonymous() && in_array($path, array('openid-test/yadis/xrds', 'openid-test/endpoint'))) {
    $menu_site_status = MENU_SITE_ONLINE;
  }
}
```

---
_Drupal 7.103 · [modules/openid/tests/openid_test.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/tests/openid_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
