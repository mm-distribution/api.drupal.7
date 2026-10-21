# menu_tree_all_data()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 1116–1162 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L1116-L1162)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_tree_all_data($menu_name, $link = NULL, $max_depth = NULL)
```

## Documentation

```text
Gets the data structure representing a named menu tree.

Since this can be the full tree including hidden items, the data returned
may be used for generating an an admin interface or a select.

@param $menu_name
  The named menu links to return
@param $link
  A fully loaded menu link, or NULL. If a link is supplied, only the
  path to root will be included in the returned tree - as if this link
  represented the current page in a visible menu.
@param $max_depth
  Optional maximum depth of links to retrieve. Typically useful if only one
  or two levels of a sub tree are needed in conjunction with a non-NULL
  $link, in which case $max_depth should be greater than $link['depth'].

@return
  An tree of menu links in an array, in the order they should be rendered.
```

## Code

```php
function menu_tree_all_data($menu_name, $link = NULL, $max_depth = NULL) {
  $tree = &drupal_static(__FUNCTION__, array());

  // Use $mlid as a flag for whether the data being loaded is for the whole tree.
  $mlid = isset($link['mlid']) ? $link['mlid'] : 0;
  // Generate a cache ID (cid) specific for this $menu_name, $link, $language, and depth.
  $cid = 'links:' . $menu_name . ':all:' . $mlid . ':' . $GLOBALS['language']->language . ':' . (int) $max_depth;

  if (!isset($tree[$cid])) {
    // If the static variable doesn't have the data, check {cache_menu}.
    $cache = cache_get($cid, 'cache_menu');
    if ($cache && isset($cache->data)) {
      // If the cache entry exists, it contains the parameters for
      // menu_build_tree().
      $tree_parameters = $cache->data;
    }
    // If the tree data was not in the cache, build $tree_parameters.
    if (!isset($tree_parameters)) {
      $tree_parameters = array(
        'min_depth' => 1,
        'max_depth' => $max_depth,
      );
      if ($mlid) {
        // The tree is for a single item, so we need to match the values in its
        // p columns and 0 (the top level) with the plid values of other links.
        $parents = array(0);
        for ($i = 1; $i < MENU_MAX_DEPTH; $i++) {
          if (!empty($link["p$i"])) {
            $parents[] = $link["p$i"];
          }
        }
        $tree_parameters['expanded'] = $parents;
        $tree_parameters['active_trail'] = $parents;
        $tree_parameters['active_trail'][] = $mlid;
      }

      // Cache the tree building parameters using the page-specific cid.
      cache_set($cid, $tree_parameters, 'cache_menu');
    }

    // Build the tree using the parameters; the resulting tree will be cached
    // by _menu_build_tree()).
    $tree[$cid] = menu_build_tree($menu_name, $tree_parameters);
  }

  return $tree[$cid];
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
