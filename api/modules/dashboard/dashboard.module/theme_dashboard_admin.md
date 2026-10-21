# theme_dashboard_admin()

- **Type:** Function
- **File:** [`modules/dashboard/dashboard.module`](_file.md), lines 609–613 · [local source](../../../../source/modules/dashboard/dashboard.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module#L609-L613)
- **Module/theme:** dashboard
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_dashboard_admin($variables)
```

## Documentation

```text
Returns HTML for the non-customizable part of the dashboard page.

@param $variables
  An associative array containing:
  - element: A render element containing a #message.

@ingroup themeable
```

## Code

```php
function theme_dashboard_admin($variables) {
  // We only return a simple help message, since the actual content of the page
  // will be populated via the dashboard regions in dashboard_page_build().
  return '<div class="customize-dashboard js-hide">' . $variables['element']['#message'] . '</div>';
}
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.module](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module) · Licensed GPL-2.0-or-later (see LICENSE)._
