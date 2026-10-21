# seven_admin_block_content()

- **Type:** Function
- **File:** [`themes/seven/template.php`](_file.md), lines 66–82 · [local source](../../../../source/themes/seven/template.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/themes/seven/template.php#L66-L82)
- **Module/theme:** seven

## Signature

```php
function seven_admin_block_content($variables)
```

## Documentation

```text
Overrides theme_admin_block_content().

Use unordered list markup in both compact and extended mode.
```

## Code

```php
function seven_admin_block_content($variables) {
  $content = $variables['content'];
  $output = '';
  if (!empty($content)) {
    $output = system_admin_compact_mode() ? '<ul class="admin-list compact">' : '<ul class="admin-list">';
    foreach ($content as $item) {
      $output .= '<li class="leaf">';
      $output .= l($item['title'], $item['href'], $item['localized_options']);
      if (isset($item['description']) && !system_admin_compact_mode()) {
        $output .= '<div class="description">' . filter_xss_admin($item['description']) . '</div>';
      }
      $output .= '</li>';
    }
    $output .= '</ul>';
  }
  return $output;
}
```

---
_Drupal 7.103 · [themes/seven/template.php](https://github.com/drupal/drupal/blob/7.103/themes/seven/template.php) · Licensed GPL-2.0-or-later (see LICENSE)._
