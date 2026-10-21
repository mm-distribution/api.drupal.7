# theme_node_recent_block()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 2352–2382 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L2352-L2382)
- **Module/theme:** node
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_node_recent_block($variables)
```

## Documentation

```text
Returns HTML for a list of recent content.

@param $variables
  An associative array containing:
  - nodes: An array of recent node objects.

@ingroup themeable
```

## Code

```php
function theme_node_recent_block($variables) {
  $rows = array();
  $output = '';

  $l_options = array('query' => drupal_get_destination());
  foreach ($variables['nodes'] as $node) {
    $row = array();
    $row[] = array(
      'data' => theme('node_recent_content', array('node' => $node)),
      'class' => 'title-author',
    );
    $row[] = array(
      'data' => node_access('update', $node) ? l(t('edit'), 'node/' . $node->nid . '/edit', $l_options) : '',
      'class' => 'edit',
    );
    $row[] = array(
      'data' => node_access('delete', $node) ? l(t('delete'), 'node/' . $node->nid . '/delete', $l_options) : '',
      'class' => 'delete',
    );
    $rows[] = $row;
  }

  if ($rows) {
    $output = theme('table', array('rows' => $rows));
    if (user_access('access content overview')) {
      $output .= theme('more_link', array('url' => 'admin/content', 'title' => t('Show more content')));
    }
  }

  return $output;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
