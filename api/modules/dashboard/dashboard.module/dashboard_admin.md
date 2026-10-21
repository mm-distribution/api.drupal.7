# dashboard_admin()

- **Type:** Function
- **File:** [`modules/dashboard/dashboard.module`](_file.md), lines 275–302 · [local source](../../../../source/modules/dashboard/dashboard.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module#L275-L302)
- **Module/theme:** dashboard

## Signature

```php
function dashboard_admin($launch_customize = FALSE)
```

## Documentation

```text
Page callback: Displays the dashboard.

@param $launch_customize
  Whether to launch in customization mode right away. TRUE or FALSE.
```

## Code

```php
function dashboard_admin($launch_customize = FALSE) {
  $js_settings = array(
    'dashboard' => array(
      'drawer' => url('admin/dashboard/drawer'),
      'blockContent' => url('admin/dashboard/block-content'),
      'updatePath' => url('admin/dashboard/update'),
      'formToken' => drupal_get_token('dashboard-update'),
      'launchCustomize' => $launch_customize,
      'dashboard' => url('admin/dashboard'),
      'emptyBlockText' => t('(empty)'),
      'emptyRegionTextInactive' => t('This dashboard region is empty. Click <em>Customize dashboard</em> to add blocks to it.'),
      'emptyRegionTextActive' => t('DRAG HERE'),
    ),
  );
  $build = array(
    '#theme' => 'dashboard_admin',
    '#message' => t('To customize the dashboard page, move blocks to the dashboard regions on the <a href="@dashboard">Dashboard administration page</a>, or enable JavaScript on this page to use the drag-and-drop interface.', array('@dashboard' => url('admin/dashboard/configure'))),
    '#access' => user_access('administer blocks'),
    '#attached' => array(
      'js' => array(
        drupal_get_path('module', 'dashboard') . '/dashboard.js',
        array('data' => $js_settings, 'type' => 'setting'),
      ),
      'library' => array(array('system', 'ui.sortable')),
    ),
  );
  return $build;
}
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.module](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module) · Licensed GPL-2.0-or-later (see LICENSE)._
