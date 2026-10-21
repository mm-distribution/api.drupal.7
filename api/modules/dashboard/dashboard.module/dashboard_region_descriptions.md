# dashboard_region_descriptions()

- **Type:** Function
- **File:** [`modules/dashboard/dashboard.module`](_file.md), lines 463–467 · [local source](../../../../source/modules/dashboard/dashboard.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module#L463-L467)
- **Module/theme:** dashboard

## Signature

```php
function dashboard_region_descriptions()
```

## Documentation

```text
Returns an array of dashboard region descriptions, keyed by region name.
```

## Code

```php
function dashboard_region_descriptions() {
  $regions = module_invoke_all('dashboard_regions');
  drupal_alter('dashboard_regions', $regions);
  return $regions;
}
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.module](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module) · Licensed GPL-2.0-or-later (see LICENSE)._
