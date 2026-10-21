# template_preprocess_dashboard_admin_display_form()

- **Type:** Function
- **File:** [`modules/dashboard/dashboard.module`](_file.md), lines 419–424 · [local source](../../../../source/modules/dashboard/dashboard.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module#L419-L424)
- **Module/theme:** dashboard

## Signature

```php
function template_preprocess_dashboard_admin_display_form(&$variables)
```

## Documentation

```text
Preprocesses variables for block-admin-display-form.tpl.php.
```

## Code

```php
function template_preprocess_dashboard_admin_display_form(&$variables) {
  template_preprocess_block_admin_display_form($variables);
  if (isset($variables['block_regions'][BLOCK_REGION_NONE])) {
    $variables['block_regions'][BLOCK_REGION_NONE] = t('Other blocks');
  }
}
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.module](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module) · Licensed GPL-2.0-or-later (see LICENSE)._
