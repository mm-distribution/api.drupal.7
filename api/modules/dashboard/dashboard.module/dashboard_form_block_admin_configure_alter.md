# dashboard_form_block_admin_configure_alter()

- **Type:** Function
- **File:** [`modules/dashboard/dashboard.module`](_file.md), lines 392–407 · [local source](../../../../source/modules/dashboard/dashboard.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module#L392-L407)
- **Module/theme:** dashboard
- **Implements:** [hook_form_FORM_ID_alter()](../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function dashboard_form_block_admin_configure_alter(&$form, &$form_state)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter().
```

## Code

```php
function dashboard_form_block_admin_configure_alter(&$form, &$form_state) {
  global $theme_key;
  drupal_theme_initialize();
  // Hide the dashboard regions from the region select list on the block
  // configuration form, for all themes except the current theme (since the
  // other themes do not display the dashboard).
  // @todo This assumes the current page is being displayed using the same
  //   theme that the dashboard is displayed in.
  $dashboard_regions = dashboard_region_descriptions();
  foreach (element_children($form['regions']) as $region_name) {
    $region = &$form['regions'][$region_name];
    if ($region_name != $theme_key && isset($region['#options'])) {
      $region['#options'] = array_diff_key($region['#options'], $dashboard_regions);
    }
  }
}
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.module](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module) · Licensed GPL-2.0-or-later (see LICENSE)._
