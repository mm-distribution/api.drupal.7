# dashboard_system_info_alter()

- **Type:** Function
- **File:** [`modules/dashboard/dashboard.module`](_file.md), lines 207–223 · [local source](../../../../source/modules/dashboard/dashboard.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module#L207-L223)
- **Module/theme:** dashboard
- **Implements:** [hook_system_info_alter()](../../system/system.api.php/hook_system_info_alter.md)

## Signature

```php
function dashboard_system_info_alter(&$info, $file, $type)
```

## Documentation

```text
Implements hook_system_info_alter().

Add regions to each theme to store the dashboard blocks.
```

## Code

```php
function dashboard_system_info_alter(&$info, $file, $type) {
  if ($type == 'theme') {
    // Add the dashboard regions (the "inactive" region should always appear
    // last in the list, for usability reasons).
    $dashboard_regions = dashboard_region_descriptions();
    if (isset($dashboard_regions['dashboard_inactive'])) {
      $inactive_region = $dashboard_regions['dashboard_inactive'];
      unset($dashboard_regions['dashboard_inactive']);
      $dashboard_regions['dashboard_inactive'] = $inactive_region;
    }
    $info['regions'] += $dashboard_regions;
    // Indicate that these regions are intended to be displayed whenever the
    // dashboard is displayed in an overlay. This information is provided for
    // any module that might need to use it, not just the core Overlay module.
    $info['overlay_regions'] = !empty($info['overlay_regions']) ? array_merge($info['overlay_regions'], dashboard_regions()) : dashboard_regions();
  }
}
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.module](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module) · Licensed GPL-2.0-or-later (see LICENSE)._
