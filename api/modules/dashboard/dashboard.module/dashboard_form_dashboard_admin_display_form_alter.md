# dashboard_form_dashboard_admin_display_form_alter()

- **Type:** Function
- **File:** [`modules/dashboard/dashboard.module`](_file.md), lines 376–387 · [local source](../../../../source/modules/dashboard/dashboard.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module#L376-L387)
- **Module/theme:** dashboard
- **Implements:** [hook_form_FORM_ID_alter()](../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function dashboard_form_dashboard_admin_display_form_alter(&$form, &$form_state)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter().
```

## Code

```php
function dashboard_form_dashboard_admin_display_form_alter(&$form, &$form_state) {
  // Redirect the 'configure' and 'delete' links on each block back to the
  // dashboard blocks administration page.
  foreach ($form['blocks'] as &$block) {
    if (isset($block['configure']['#href'])) {
      $block['configure']['#options']['query']['destination'] = 'admin/dashboard/configure';
    }
    if (isset($block['delete']['#href'])) {
      $block['delete']['#options']['query']['destination'] = 'admin/dashboard/configure';
    }
  }
}
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.module](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module) · Licensed GPL-2.0-or-later (see LICENSE)._
