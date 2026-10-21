# dashboard_theme()

- **Type:** Function
- **File:** [`modules/dashboard/dashboard.module`](_file.md), lines 228–254 · [local source](../../../../source/modules/dashboard/dashboard.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module#L228-L254)
- **Module/theme:** dashboard
- **Implements:** [hook_theme()](../../system/system.api.php/hook_theme.md)

## Signature

```php
function dashboard_theme()
```

## Documentation

```text
Implements hook_theme().
```

## Code

```php
function dashboard_theme() {
  return array(
    'dashboard' => array(
      'render element' => 'element',
    ),
    'dashboard_admin' => array(
      'render element' => 'element',
    ),
    'dashboard_region' => array(
      'render element' => 'element',
    ),
    'dashboard_disabled_blocks' => array(
      'variables' => array('blocks' => NULL),
    ),
    'dashboard_disabled_block' => array(
      'variables' => array('block' => NULL),
    ),
    'dashboard_admin_display_form' => array(
      // When building the form for configuring dashboard blocks, reuse the
      // Block module's template for the main block configuration form.
      'template' => 'block-admin-display-form',
      'path' => drupal_get_path('module', 'block'),
      'file' => 'block.admin.inc',
      'render element' => 'form',
    ),
  );
}
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.module](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module) · Licensed GPL-2.0-or-later (see LICENSE)._
