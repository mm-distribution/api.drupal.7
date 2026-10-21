# menu_build_tree()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 1362–1368 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L1362-L1368)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_build_tree($menu_name, array $parameters = array())
```

## Documentation

```text
Builds a menu tree, translates links, and checks access.

@param $menu_name
  The name of the menu.
@param $parameters
  (optional) An associative array of build parameters. Possible keys:
  - expanded: An array of parent link ids to return only menu links that are
    children of one of the plids in this list. If empty, the whole menu tree
    is built, unless 'only_active_trail' is TRUE.
  - active_trail: An array of mlids, representing the coordinates of the
    currently active menu link.
  - only_active_trail: Whether to only return links that are in the active
    trail. This option is ignored, if 'expanded' is non-empty. Internally
    used for breadcrumbs.
  - min_depth: The minimum depth of menu links in the resulting tree.
    Defaults to 1, which is the default to build a whole tree for a menu
    (excluding menu container itself).
  - max_depth: The maximum depth of menu links in the resulting tree.
  - conditions: An associative array of custom database select query
    condition key/value pairs; see _menu_build_tree() for the actual query.

@return
  A fully built menu tree.
```

## Code

```php
function menu_build_tree($menu_name, array $parameters = array()) {
  // Build the menu tree.
  $data = _menu_build_tree($menu_name, $parameters);
  // Check access for the current user to each item in the tree.
  menu_tree_check_access($data['tree'], $data['node_links']);
  return $data['tree'];
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
