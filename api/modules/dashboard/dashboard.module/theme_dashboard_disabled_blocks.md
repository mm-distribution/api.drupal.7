# theme_dashboard_disabled_blocks()

- **Type:** Function
- **File:** [`modules/dashboard/dashboard.module`](_file.md), lines 646–657 · [local source](../../../../source/modules/dashboard/dashboard.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module#L646-L657)
- **Module/theme:** dashboard
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_dashboard_disabled_blocks($variables)
```

## Documentation

```text
Returns HTML for disabled blocks, for use in dashboard customization mode.

@param $variables
  An associative array containing:
  - blocks: An array of block objects from _block_rehash().

@ingroup themeable
```

## Code

```php
function theme_dashboard_disabled_blocks($variables) {
  extract($variables);
  $output = '<div class="canvas-content"><p>' . t('Drag and drop these blocks to the columns below. Changes are automatically saved. More options are available on the <a href="@dashboard-url">configuration page</a>.', array('@dashboard-url' => url('admin/dashboard/configure'))) . '</p>';
  $output .= '<div id="disabled-blocks"><div class="region disabled-blocks clearfix">';
  foreach ($blocks as $block) {
    $output .= theme('dashboard_disabled_block', array('block' => $block));
  }
  $output .= '<div class="clearfix"></div>';
  $output .= '<p class="dashboard-add-other-blocks">' . l(t('Add other blocks'), 'admin/dashboard/configure') . '</p>';
  $output .= '</div></div></div>';
  return $output;
}
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.module](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module) · Licensed GPL-2.0-or-later (see LICENSE)._
