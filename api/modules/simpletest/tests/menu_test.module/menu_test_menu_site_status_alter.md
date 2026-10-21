# menu_test_menu_site_status_alter()

- **Type:** Function
- **File:** [`modules/simpletest/tests/menu_test.module`](_file.md), lines 539–544 · [local source](../../../../../source/modules/simpletest/tests/menu_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu_test.module#L539-L544)
- **Module/theme:** batch_test
- **Implements:** [hook_menu_site_status_alter()](../../../system/system.api.php/hook_menu_site_status_alter.md)

## Signature

```php
function menu_test_menu_site_status_alter(&$menu_site_status, $path)
```

## Documentation

```text
Implements hook_menu_site_status_alter().
```

## Code

```php
function menu_test_menu_site_status_alter(&$menu_site_status, $path) {
  // Allow access to ?q=menu_login_callback even if in maintenance mode.
  if ($menu_site_status == MENU_SITE_OFFLINE && $path == 'menu_login_callback') {
    $menu_site_status = MENU_SITE_ONLINE;
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
