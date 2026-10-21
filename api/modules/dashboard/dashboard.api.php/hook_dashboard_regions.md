# hook_dashboard_regions()

- **Type:** Hook (documentation function)
- **File:** [`modules/dashboard/dashboard.api.php`](_file.md), lines 21–26 · [local source](../../../../source/modules/dashboard/dashboard.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.api.php#L21-L26)
- **Module/theme:** dashboard
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_dashboard_regions()
```

## Documentation

```text
Add regions to the dashboard.

@return
  An array whose keys are the names of the dashboard regions and whose
  values are the titles that will be displayed in the blocks administration
  interface. The keys are also used as theme wrapper functions.
```

## Code

```php
function hook_dashboard_regions() {
  // Define a new dashboard region. Your module can also then define
  // theme_mymodule_dashboard_region() as a theme wrapper function to control
  // the region's appearance.
  return array('mymodule_dashboard_region' => "My module's dashboard region");
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_dashboard_regions()".

- [dashboard_dashboard_regions()](../dashboard.module/dashboard_dashboard_regions.md) — `modules/dashboard/dashboard.module`

---
_Drupal 7.103 · [modules/dashboard/dashboard.api.php](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
