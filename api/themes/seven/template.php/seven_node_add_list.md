# seven_node_add_list()

- **Type:** Function
- **File:** [`themes/seven/template.php`](_file.md), lines 42–59 · [local source](../../../../source/themes/seven/template.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/themes/seven/template.php#L42-L59)
- **Module/theme:** seven

## Signature

```php
function seven_node_add_list($variables)
```

## Documentation

```text
Display the list of available node types for node creation.
```

## Code

```php
function seven_node_add_list($variables) {
  $content = $variables['content'];
  $output = '';
  if ($content) {
    $output = '<ul class="admin-list">';
    foreach ($content as $item) {
      $output .= '<li class="clearfix">';
      $output .= '<span class="label">' . l($item['title'], $item['href'], $item['localized_options']) . '</span>';
      $output .= '<div class="description">' . filter_xss_admin($item['description']) . '</div>';
      $output .= '</li>';
    }
    $output .= '</ul>';
  }
  else {
    $output = '<p>' . t('You have not created any content types yet. Go to the <a href="@create-content">content type creation page</a> to add a new content type.', array('@create-content' => url('admin/structure/types/add'))) . '</p>';
  }
  return $output;
}
```

---
_Drupal 7.103 · [themes/seven/template.php](https://github.com/drupal/drupal/blob/7.103/themes/seven/template.php) · Licensed GPL-2.0-or-later (see LICENSE)._
