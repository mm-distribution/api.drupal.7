# dashboard_form_block_admin_display_form_alter()

- **Type:** Function
- **File:** [`modules/dashboard/dashboard.module`](_file.md), lines 341–371 · [local source](../../../../source/modules/dashboard/dashboard.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module#L341-L371)
- **Module/theme:** dashboard
- **Implements:** [hook_form_FORM_ID_alter()](../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function dashboard_form_block_admin_display_form_alter(&$form, &$form_state, $form_id)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter().
```

## Code

```php
function dashboard_form_block_admin_display_form_alter(&$form, &$form_state, $form_id) {
  // Hide dashboard regions (and any blocks placed within them) from the block
  // administration form and from the options list on that form. This
  // function is called for both the dashboard block configuration form and the
  // standard block configuration form so that both forms can share the same
  // constructor. As a result the form_id must be checked.
  if ($form_id != 'dashboard_admin_display_form') {
    $dashboard_regions = dashboard_region_descriptions();
    $form['block_regions']['#value'] = array_diff_key($form['block_regions']['#value'], $dashboard_regions);
    foreach (element_children($form['blocks']) as $i) {
      $block = &$form['blocks'][$i];
      if (isset($block['region']['#default_value']) && isset($dashboard_regions[$block['region']['#default_value']]) && $block['region']['#default_value'] != 'dashboard_inactive') {
        $block['#access'] = FALSE;
      }
      elseif (isset($block['region']['#options'])) {
        $block['region']['#options'] = array_diff_key($block['region']['#options'], $dashboard_regions);
      }
      // Show inactive dashboard blocks as disabled on the main block
      // administration form, so that they are available to place in other
      // regions of the theme. Note that when the form is submitted, any such
      // blocks which still remain disabled will immediately be put back in the
      // 'dashboard_inactive' region, because dashboard_block_info_alter() is
      // called when the blocks are rehashed. Fortunately, this is the exact
      // behavior we want.
      if ($block['region']['#default_value'] == 'dashboard_inactive') {
        // @todo These do not wind up in correct alphabetical order.
        $block['region']['#default_value'] = NULL;
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.module](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module) · Licensed GPL-2.0-or-later (see LICENSE)._
