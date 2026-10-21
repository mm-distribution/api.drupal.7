# theme_dashboard_region()

- **Type:** Function
- **File:** [`modules/dashboard/dashboard.module`](_file.md), lines 625–635 · [local source](../../../../source/modules/dashboard/dashboard.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module#L625-L635)
- **Module/theme:** dashboard
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_dashboard_region($variables)
```

## Documentation

```text
Returns HTML for a generic dashboard region.

@param $variables
  An associative array containing:
  - element: A render element containing the properties of the dashboard
    region element, #dashboard_region and #children.

@ingroup themeable
```

## Code

```php
function theme_dashboard_region($variables) {
  extract($variables);
  $output = '<div id="' . $element['#dashboard_region'] . '" class="dashboard-region">';
  $output .= '<div class="region clearfix">';
  $output .= $element['#children'];
  // Closing div.region
  $output .= '</div>';
  // Closing div.dashboard-region
  $output .= '</div>';
  return $output;
}
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.module](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module) · Licensed GPL-2.0-or-later (see LICENSE)._
