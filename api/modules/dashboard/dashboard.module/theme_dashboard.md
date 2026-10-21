# theme_dashboard()

- **Type:** Function
- **File:** [`modules/dashboard/dashboard.module`](_file.md), lines 594–598 · [local source](../../../../source/modules/dashboard/dashboard.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module#L594-L598)
- **Module/theme:** dashboard
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_dashboard($variables)
```

## Documentation

```text
Returns HTML for the entire dashboard.

@param $variables
  An associative array containing:
  - element: A render element containing the properties of the dashboard
    region element, #dashboard_region and #children.

@ingroup themeable
```

## Code

```php
function theme_dashboard($variables) {
  extract($variables);
  drupal_add_css(drupal_get_path('module', 'dashboard') . '/dashboard.css');
  return '<div id="dashboard" class="clearfix">' . $element['#children'] . '</div>';
}
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.module](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module) · Licensed GPL-2.0-or-later (see LICENSE)._
