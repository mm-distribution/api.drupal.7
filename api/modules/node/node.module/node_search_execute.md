# node_search_execute()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 1699–1754 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L1699-L1754)
- **Module/theme:** node
- **Implements:** [hook_search_execute()](../../search/search.api.php/hook_search_execute.md)

## Signature

```php
function node_search_execute($keys = NULL, $conditions = NULL)
```

## Documentation

```text
Implements hook_search_execute().
```

## Code

```php
function node_search_execute($keys = NULL, $conditions = NULL) {
  // Build matching conditions
  $query = db_select('search_index', 'i', array('target' => 'slave'))->extend('SearchQuery')->extend('PagerDefault');
  $query->join('node', 'n', 'n.nid = i.sid');
  $query
    ->condition('n.status', 1)
    ->addTag('node_access')
    ->searchExpression($keys, 'node');

  // Insert special keywords.
  $query->setOption('type', 'n.type');
  $query->setOption('language', 'n.language');
  if ($query->setOption('term', 'ti.tid')) {
    $query->join('taxonomy_index', 'ti', 'n.nid = ti.nid');
  }
  // Only continue if the first pass query matches.
  if (!$query->executeFirstPass()) {
    return array();
  }

  // Add the ranking expressions.
  _node_rankings($query);

  // Load results.
  $find = $query
    ->limit(10)
    ->execute();
  $results = array();
  foreach ($find as $item) {
    // Render the node.
    $node = node_load($item->sid);
    $build = node_view($node, 'search_result');
    unset($build['#theme']);
    $node->rendered = drupal_render($build);

    // Fetch comments for snippet.
    $node->rendered .= ' ' . module_invoke('comment', 'node_update_index', $node);

    $extra = module_invoke_all('node_search_result', $node);

    $uri = entity_uri('node', $node);
    $results[] = array(
      'link' => url($uri['path'], array_merge($uri['options'], array('absolute' => TRUE))),
      'type' => check_plain(node_type_get_name($node)),
      'title' => $node->title,
      'user' => theme('username', array('account' => $node)),
      'date' => $node->changed,
      'node' => $node,
      'extra' => $extra,
      'score' => $item->calculated_score,
      'snippet' => search_excerpt($keys, $node->rendered),
      'language' => entity_language('node', $node),
    );
  }
  return $results;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
