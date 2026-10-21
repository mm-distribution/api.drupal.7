# dashboard_forms()

- **Type:** Function
- **File:** [`modules/dashboard/dashboard.module`](_file.md), lines 259–267 · [local source](../../../../source/modules/dashboard/dashboard.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module#L259-L267)
- **Module/theme:** dashboard
- **Implements:** [hook_forms()](../../system/system.api.php/hook_forms.md)

## Signature

```php
function dashboard_forms()
```

## Documentation

```text
Implements hook_forms().
```

## Code

```php
function dashboard_forms() {
  // Reroute the dashboard configuration form to the main blocks administration
  // form. This allows us to distinguish them by form ID in hook_form_alter().
  $forms['dashboard_admin_display_form'] = array(
    'callback' => 'block_admin_display_form',
  );

  return $forms;
}
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.module](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module) · Licensed GPL-2.0-or-later (see LICENSE)._
