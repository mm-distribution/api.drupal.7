# menu_tree_data()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 1577–1581 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L1577-L1581)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_tree_data(array $links, array $parents = array(), $depth = 1)
```

## Documentation

```text
Sorts and returns the built data representing a menu tree.

@param $links
  A flat array of menu links that are part of the menu. Each array element
  is an associative array of information about the menu link, containing the
  fields from the {menu_links} table, and optionally additional information
  from the {menu_router} table, if the menu item appears in both tables.
  This array must be ordered depth-first. See _menu_build_tree() for a sample
  query.
@param $parents
  An array of the menu link ID values that are in the path from the current
  page to the root of the menu tree.
@param $depth
  The minimum depth to include in the returned menu tree.

@return
  An array of menu links in the form of a tree. Each item in the tree is an
  associative array containing:
  - link: The menu link item from $links, with additional element
    'in_active_trail' (TRUE if the link ID was in $parents).
  - below: An array containing the sub-tree of this item, where each element
    is a tree item array with 'link' and 'below' elements. This array will be
    empty if the menu item has no items in its sub-tree having a depth
    greater than or equal to $depth.
```

## Code

```php
function menu_tree_data(array $links, array $parents = array(), $depth = 1) {
  // Reverse the array so we can use the more efficient array_pop() function.
  $links = array_reverse($links);
  return _menu_tree_data($links, $parents, $depth);
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
