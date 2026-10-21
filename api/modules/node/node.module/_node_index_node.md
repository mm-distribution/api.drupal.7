# _node_index_node()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 2783–2805 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L2783-L2805)
- **Module/theme:** node

## Signature

```php
function _node_index_node($node)
```

## Documentation

```text
Indexes a single node.

@param $node
  The node to index.
```

## Code

```php
function _node_index_node($node) {
  $node = node_load($node->nid);

  // Save the changed time of the most recent indexed node, for the search
  // results half-life calculation.
  variable_set('node_cron_last', $node->changed);

  // Render the node.
  $build = node_view($node, 'search_index');
  unset($build['#theme']);
  $node->rendered = drupal_render($build);

  $text = '<h1>' . check_plain($node->title) . '</h1>' . $node->rendered;

  // Fetch extra data normally not visible
  $extra = module_invoke_all('node_update_index', $node);
  foreach ($extra as $t) {
    $text .= $t;
  }

  // Update index
  search_index($node->nid, 'node', $text);
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
