# dashboard_menu()

- **Type:** Function
- **File:** [`modules/dashboard/dashboard.module`](_file.md), lines 36–79 · [local source](../../../../source/modules/dashboard/dashboard.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module#L36-L79)
- **Module/theme:** dashboard
- **Implements:** [hook_menu()](../../system/system.api.php/hook_menu.md)

## Signature

```php
function dashboard_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function dashboard_menu() {
  $items['admin/dashboard'] = array(
    'title' => 'Dashboard',
    'description' => 'View and customize your dashboard.',
    'page callback' => 'dashboard_admin',
    'access arguments' => array('access dashboard'),
    // Make this appear first, so for example, in admin menus, it shows up on
    // the top corner of the window as a convenient "home link".
    'weight' => -15,
  );
  $items['admin/dashboard/configure'] = array(
    'title' => 'Configure available dashboard blocks',
    'description' => 'Configure which blocks can be shown on the dashboard.',
    'page callback' => 'dashboard_admin_blocks',
    'access arguments' => array('administer blocks'),
    'type' => MENU_VISIBLE_IN_BREADCRUMB,
  );
  $items['admin/dashboard/customize'] = array(
    'title' => 'Customize dashboard',
    'description' => 'Customize your dashboard.',
    'page callback' => 'dashboard_admin',
    'page arguments' => array(TRUE),
    'access arguments' => array('access dashboard'),
    'type' => MENU_VISIBLE_IN_BREADCRUMB,
  );
  $items['admin/dashboard/drawer'] = array(
    'page callback' => 'dashboard_show_disabled',
    'access arguments' => array('administer blocks'),
    'type' => MENU_CALLBACK,
  );
  $items['admin/dashboard/block-content/%/%'] = array(
    'page callback' => 'dashboard_show_block_content',
    'page arguments' => array(3, 4),
    'access arguments' => array('administer blocks'),
    'type' => MENU_CALLBACK,
  );
  $items['admin/dashboard/update'] = array(
    'page callback' => 'dashboard_update',
    'access arguments' => array('administer blocks'),
    'type' => MENU_CALLBACK,
  );

  return $items;
}
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.module](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module) · Licensed GPL-2.0-or-later (see LICENSE)._
