# theme_dashboard_disabled_block()

- **Type:** Function
- **File:** [`modules/dashboard/dashboard.module`](_file.md), lines 668–680 · [local source](../../../../source/modules/dashboard/dashboard.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module#L668-L680)
- **Module/theme:** dashboard
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_dashboard_disabled_block($variables)
```

## Documentation

```text
Returns HTML for disabled blocks, for use in dashboard customization mode.

@param $variables
  An associative array containing:
  - block: A block object from _block_rehash().

@ingroup themeable
```

## Code

```php
function theme_dashboard_disabled_block($variables) {
  extract($variables);
  $output = "";
  if (isset($block)) {
    $output .= '<div id="block-' . $block['module'] . '-' . $block['delta']
    . '" class="disabled-block block block-' . $block['module'] . '-' . $block['delta']
    . ' module-' . $block['module'] . ' delta-' . $block['delta'] . '">'
    . '<h2>' . (!empty($block['title']) && $block['title'] != '<none>' ? check_plain($block['title']) : check_plain($block['info'])) . '</h2>'
    . '<div class="content"></div>'
    . '</div>';
  }
  return $output;
}
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.module](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module) · Licensed GPL-2.0-or-later (see LICENSE)._
