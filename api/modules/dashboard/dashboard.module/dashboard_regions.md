# dashboard_regions()

- **Type:** Function
- **File:** [`modules/dashboard/dashboard.module`](_file.md), lines 472–478 · [local source](../../../../source/modules/dashboard/dashboard.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module#L472-L478)
- **Module/theme:** dashboard

## Signature

```php
function dashboard_regions()
```

## Documentation

```text
Returns an array of dashboard region names.
```

## Code

```php
function dashboard_regions() {
  $regions = &drupal_static(__FUNCTION__);
  if (!isset($regions)) {
    $regions = array_keys(dashboard_region_descriptions());
  }
  return $regions;
}
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.module](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module) · Licensed GPL-2.0-or-later (see LICENSE)._
