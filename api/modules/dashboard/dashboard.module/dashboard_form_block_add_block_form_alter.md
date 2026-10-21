# dashboard_form_block_add_block_form_alter()

- **Type:** Function
- **File:** [`modules/dashboard/dashboard.module`](_file.md), lines 412–414 · [local source](../../../../source/modules/dashboard/dashboard.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module#L412-L414)
- **Module/theme:** dashboard
- **Implements:** [hook_form_FORM_ID_alter()](../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function dashboard_form_block_add_block_form_alter(&$form, &$form_state)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter().
```

## Code

```php
function dashboard_form_block_add_block_form_alter(&$form, &$form_state) {
  dashboard_form_block_admin_configure_alter($form, $form_state);
}
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.module](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module) · Licensed GPL-2.0-or-later (see LICENSE)._
