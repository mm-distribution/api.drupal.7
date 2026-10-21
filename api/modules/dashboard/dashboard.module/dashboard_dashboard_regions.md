# dashboard_dashboard_regions()

- **Type:** Function
- **File:** [`modules/dashboard/dashboard.module`](_file.md), lines 483–489 · [local source](../../../../source/modules/dashboard/dashboard.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module#L483-L489)
- **Module/theme:** dashboard
- **Implements:** [hook_dashboard_regions()](../dashboard.api.php/hook_dashboard_regions.md)

## Signature

```php
function dashboard_dashboard_regions()
```

## Documentation

```text
Implements hook_dashboard_regions().
```

## Code

```php
function dashboard_dashboard_regions() {
  return array(
    'dashboard_main' => 'Dashboard (main)',
    'dashboard_sidebar' => 'Dashboard (sidebar)',
    'dashboard_inactive' => 'Dashboard (inactive)',
  );
}
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.module](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module) · Licensed GPL-2.0-or-later (see LICENSE)._
