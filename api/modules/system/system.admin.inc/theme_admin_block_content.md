# theme_admin_block_content()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 2470–2489 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L2470-L2489)
- **Module/theme:** system
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_admin_block_content($variables)
```

## Documentation

```text
Returns HTML for the content of an administrative block.

@param $variables
  An associative array containing:
  - content: An array containing information about the block. Each element
    of the array represents an administrative menu item, and must at least
    contain the keys 'title', 'href', and 'localized_options', which are
    passed to l(). A 'description' key may also be provided.

@ingroup themeable
```

## Code

```php
function theme_admin_block_content($variables) {
  $content = $variables['content'];
  $output = '';

  if (!empty($content)) {
    $class = 'admin-list';
    if ($compact = system_admin_compact_mode()) {
      $class .= ' compact';
    }
    $output .= '<dl class="' . $class . '">';
    foreach ($content as $item) {
      $output .= '<dt>' . l($item['title'], $item['href'], $item['localized_options']) . '</dt>';
      if (!$compact && isset($item['description'])) {
        $output .= '<dd>' . filter_xss_admin($item['description']) . '</dd>';
      }
    }
    $output .= '</dl>';
  }
  return $output;
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
