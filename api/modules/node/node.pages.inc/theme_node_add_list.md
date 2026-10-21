# theme_node_add_list()

- **Type:** Function
- **File:** [`modules/node/node.pages.inc`](_file.md), lines 44–60 · [local source](../../../../source/modules/node/node.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.pages.inc#L44-L60)
- **Module/theme:** node
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_node_add_list($variables)
```

## Documentation

```text
Returns HTML for a list of available node types for node creation.

@param $variables
  An associative array containing:
  - content: An array of content types.

@ingroup themeable
```

## Code

```php
function theme_node_add_list($variables) {
  $content = $variables['content'];
  $output = '';

  if ($content) {
    $output = '<dl class="node-type-list">';
    foreach ($content as $item) {
      $output .= '<dt>' . l($item['title'], $item['href'], $item['localized_options']) . '</dt>';
      $output .= '<dd>' . filter_xss_admin($item['description']) . '</dd>';
    }
    $output .= '</dl>';
  }
  else {
    $output = '<p>' . t('You have not created any content types yet. Go to the <a href="@create-content">content type creation page</a> to add a new content type.', array('@create-content' => url('admin/structure/types/add'))) . '</p>';
  }
  return $output;
}
```

---
_Drupal 7.103 · [modules/node/node.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/node.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
