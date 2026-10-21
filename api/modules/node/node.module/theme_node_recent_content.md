# theme_node_recent_content()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 2393–2404 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L2393-L2404)
- **Module/theme:** node
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_node_recent_content($variables)
```

## Documentation

```text
Returns HTML for a recent node to be displayed in the recent content block.

@param $variables
  An associative array containing:
  - node: A node object.

@ingroup themeable
```

## Code

```php
function theme_node_recent_content($variables) {
  $node = $variables['node'];

  $output = '<div class="node-title">';
  $output .= l($node->title, 'node/' . $node->nid);
  $output .= theme('mark', array('type' => node_mark($node->nid, $node->changed)));
  $output .= '</div><div class="node-author">';
  $output .= theme('username', array('account' => user_load($node->uid)));
  $output .= '</div>';

  return $output;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
