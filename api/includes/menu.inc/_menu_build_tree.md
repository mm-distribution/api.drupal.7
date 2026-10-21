# _menu_build_tree()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 1379–1464 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L1379-L1464)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function _menu_build_tree($menu_name, array $parameters = array())
```

## Documentation

```text
Builds a menu tree.

This function may be used build the data for a menu tree only, for example
to further massage the data manually before further processing happens.
menu_tree_check_access() needs to be invoked afterwards.

@see menu_build_tree()
```

## Code

```php
function _menu_build_tree($menu_name, array $parameters = array()) {
  // Static cache of already built menu trees.
  $trees = &drupal_static(__FUNCTION__, array());

  // Build the cache id; sort parents to prevent duplicate storage and remove
  // default parameter values.
  if (isset($parameters['expanded'])) {
    sort($parameters['expanded']);
  }
  $tree_cid = 'links:' . $menu_name . ':tree-data:' . $GLOBALS['language']->language . ':' . hash('sha256', serialize($parameters));

  // If we do not have this tree in the static cache, check {cache_menu}.
  if (!isset($trees[$tree_cid])) {
    $cache = cache_get($tree_cid, 'cache_menu');
    if ($cache && isset($cache->data)) {
      $trees[$tree_cid] = $cache->data;
    }
  }

  if (!isset($trees[$tree_cid])) {
    // Select the links from the table, and recursively build the tree. We
    // LEFT JOIN since there is no match in {menu_router} for an external
    // link.
    $query = db_select('menu_links', 'ml', array('fetch' => PDO::FETCH_ASSOC));
    $query->addTag('translatable');
    $query->leftJoin('menu_router', 'm', 'm.path = ml.router_path');
    $query->fields('ml');
    $query->fields('m', array(
      'load_functions',
      'to_arg_functions',
      'access_callback',
      'access_arguments',
      'page_callback',
      'page_arguments',
      'delivery_callback',
      'tab_parent',
      'tab_root',
      'title',
      'title_callback',
      'title_arguments',
      'theme_callback',
      'theme_arguments',
      'type',
      'description',
    ));
    for ($i = 1; $i <= MENU_MAX_DEPTH; $i++) {
      $query->orderBy('p' . $i, 'ASC');
    }
    $query->condition('ml.menu_name', $menu_name);
    if (!empty($parameters['expanded'])) {
      $query->condition('ml.plid', $parameters['expanded'], 'IN');
    }
    elseif (!empty($parameters['only_active_trail'])) {
      $query->condition('ml.mlid', $parameters['active_trail'], 'IN');
    }
    $min_depth = (isset($parameters['min_depth']) ? $parameters['min_depth'] : 1);
    if ($min_depth != 1) {
      $query->condition('ml.depth', $min_depth, '>=');
    }
    if (isset($parameters['max_depth'])) {
      $query->condition('ml.depth', $parameters['max_depth'], '<=');
    }
    // Add custom query conditions, if any were passed.
    if (isset($parameters['conditions'])) {
      foreach ($parameters['conditions'] as $column => $value) {
        $query->condition($column, $value);
      }
    }

    // Build an ordered array of links using the query result object.
    $links = array();
    foreach ($query->execute() as $item) {
      $links[] = $item;
    }
    $active_trail = (isset($parameters['active_trail']) ? $parameters['active_trail'] : array());
    $data['tree'] = menu_tree_data($links, $active_trail, $min_depth);
    $data['node_links'] = array();
    menu_tree_collect_node_links($data['tree'], $data['node_links']);

    // Cache the data, if it is not already in the cache.
    cache_set($tree_cid, $data, 'cache_menu');
    $trees[$tree_cid] = $data;
  }

  return $trees[$tree_cid];
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
