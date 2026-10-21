# _menu_tree_data()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 1589–1616 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L1589-L1616)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function _menu_tree_data(&$links, $parents, $depth)
```

## Documentation

```text
Builds the data representing a menu tree.

The function is a bit complex because the rendering of a link depends on
the next menu link.
```

## Code

```php
function _menu_tree_data(&$links, $parents, $depth) {
  $tree = array();
  while ($item = array_pop($links)) {
    // We need to determine if we're on the path to root so we can later build
    // the correct active trail and breadcrumb.
    $item['in_active_trail'] = in_array($item['mlid'], $parents);
    // Add the current link to the tree.
    $tree[$item['mlid']] = array(
      'link' => $item,
      'below' => array(),
    );
    // Look ahead to the next link, but leave it on the array so it's available
    // to other recursive function calls if we return or build a sub-tree.
    $next = end($links);
    // Check whether the next link is the first in a new sub-tree.
    if ($next && $next['depth'] > $depth) {
      // Recursively call _menu_tree_data to build the sub-tree.
      $tree[$item['mlid']]['below'] = _menu_tree_data($links, $parents, $next['depth']);
      // Fetch next link after filling the sub-tree.
      $next = end($links);
    }
    // Determine if we should exit the loop and return.
    if (!$next || $next['depth'] < $depth) {
      break;
    }
  }
  return $tree;
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
