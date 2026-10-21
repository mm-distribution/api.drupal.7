# hook_dashboard_regions_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/dashboard/dashboard.api.php`](_file.md), lines 35–38 · [local source](../../../../source/modules/dashboard/dashboard.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.api.php#L35-L38)
- **Module/theme:** dashboard
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_dashboard_regions_alter(&$regions)
```

## Documentation

```text
Alter dashboard regions provided by modules.

@param $regions
  An array containing all dashboard regions, in the format provided by
  hook_dashboard_regions().
```

## Code

```php
function hook_dashboard_regions_alter(&$regions) {
  // Remove the sidebar region defined by the core dashboard module.
  unset($regions['dashboard_sidebar']);
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_dashboard_regions_alter()".

_None found._

---
_Drupal 7.103 · [modules/dashboard/dashboard.api.php](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
