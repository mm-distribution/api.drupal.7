# book_menu_subtree_data()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 1383–1440 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L1383-L1440)
- **Module/theme:** book

## Signature

```php
function book_menu_subtree_data($link)
```

## Documentation

```text
Gets the data representing a subtree of the book hierarchy.

The root of the subtree will be the link passed as a parameter, so the
returned tree will contain this item and all its descendents in the menu
tree.

@param $link
  A fully loaded menu link.

@return
  A subtree of menu links in an array, in the order they should be rendered.
```

## Code

```php
function book_menu_subtree_data($link) {
  $tree = &drupal_static(__FUNCTION__, array());

  // Generate a cache ID (cid) specific for this $menu_name and $link.
  $cid = 'links:' . $link['menu_name'] . ':subtree-cid:' . $link['mlid'];

  if (!isset($tree[$cid])) {
    $cache = cache_get($cid, 'cache_menu');

    if ($cache && isset($cache->data)) {
      // If the cache entry exists, it will just be the cid for the actual data.
      // This avoids duplication of large amounts of data.
      $cache = cache_get($cache->data, 'cache_menu');

      if ($cache && isset($cache->data)) {
        $data = $cache->data;
      }
    }

    // If the subtree data was not in the cache, $data will be NULL.
    if (!isset($data)) {
      $query = db_select('menu_links', 'ml', array('fetch' => PDO::FETCH_ASSOC));
      $query->join('menu_router', 'm', 'm.path = ml.router_path');
      $query->join('book', 'b', 'ml.mlid = b.mlid');
      $query->fields('b');
      $query->fields('m', array('load_functions', 'to_arg_functions', 'access_callback', 'access_arguments', 'page_callback', 'page_arguments', 'delivery_callback', 'title', 'title_callback', 'title_arguments', 'type'));
      $query->fields('ml');
      $query->condition('menu_name', $link['menu_name']);
      for ($i = 1; $i <= MENU_MAX_DEPTH && $link["p$i"]; ++$i) {
        $query->condition("p$i", $link["p$i"]);
      }
      for ($i = 1; $i <= MENU_MAX_DEPTH; ++$i) {
        $query->orderBy("p$i");
      }
      $links = array();
      foreach ($query->execute() as $item) {
        $links[] = $item;
      }
      $data['tree'] = menu_tree_data($links, array(), $link['depth']);
      $data['node_links'] = array();
      menu_tree_collect_node_links($data['tree'], $data['node_links']);
      // Compute the real cid for book subtree data.
      $tree_cid = 'links:' . $item['menu_name'] . ':subtree-data:' . hash('sha256', serialize($data));
      // Cache the data, if it is not already in the cache.

      if (!cache_get($tree_cid, 'cache_menu')) {
        cache_set($tree_cid, $data, 'cache_menu');
      }
      // Cache the cid of the (shared) data using the menu and item-specific cid.
      cache_set($cid, $tree_cid, 'cache_menu');
    }
    // Check access for the current user to each item in the tree.
    menu_tree_check_access($data['tree'], $data['node_links']);
    $tree[$cid] = $data['tree'];
  }

  return $tree[$cid];
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
