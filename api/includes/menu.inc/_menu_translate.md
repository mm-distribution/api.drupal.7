# _menu_translate()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 764–809 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L764-L809)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function _menu_translate(&$router_item, $map, $to_arg = FALSE)
```

## Documentation

```text
Handles dynamic path translation and menu access control.

When a user arrives on a page such as node/5, this function determines
what "5" corresponds to, by inspecting the page's menu path definition,
node/%node. This will call node_load(5) to load the corresponding node
object.

It also works in reverse, to allow the display of tabs and menu items which
contain these dynamic arguments, translating node/%node to node/5.

Translation of menu item titles and descriptions are done here to
allow for storage of English strings in the database, and translation
to the language required to generate the current page.

@param $router_item
  A menu router item
@param $map
  An array of path arguments; for example, array('node', '5').
@param $to_arg
  Execute $item['to_arg_functions'] or not. Use only if you want to render a
  path from the menu table, for example tabs.

@return
  Returns the map with objects loaded as defined in the
  $item['load_functions']. $item['access'] becomes TRUE if the item is
  accessible, FALSE otherwise. $item['href'] is set according to the map.
  If an error occurs during calling the load_functions (like trying to load
  a non-existent node) then this function returns FALSE.
```

## Code

```php
function _menu_translate(&$router_item, $map, $to_arg = FALSE) {
  if ($to_arg && !empty($router_item['to_arg_functions'])) {
    // Fill in missing path elements, such as the current uid.
    _menu_link_map_translate($map, $router_item['to_arg_functions']);
  }
  // The $path_map saves the pieces of the path as strings, while elements in
  // $map may be replaced with loaded objects.
  $path_map = $map;
  if (!empty($router_item['load_functions']) && !_menu_load_objects($router_item, $map)) {
    // An error occurred loading an object.
    $router_item['access'] = FALSE;
    return FALSE;
  }

  // Generate the link path for the page request or local tasks.
  $link_map = explode('/', $router_item['path']);
  if (isset($router_item['tab_root'])) {
    $tab_root_map = explode('/', $router_item['tab_root']);
  }
  if (isset($router_item['tab_parent'])) {
    $tab_parent_map = explode('/', $router_item['tab_parent']);
  }
  for ($i = 0; $i < $router_item['number_parts']; $i++) {
    if ($link_map[$i] == '%') {
      $link_map[$i] = $path_map[$i];
    }
    if (isset($tab_root_map[$i]) && $tab_root_map[$i] == '%') {
      $tab_root_map[$i] = $path_map[$i];
    }
    if (isset($tab_parent_map[$i]) && $tab_parent_map[$i] == '%') {
      $tab_parent_map[$i] = $path_map[$i];
    }
  }
  $router_item['href'] = implode('/', $link_map);
  $router_item['tab_root_href'] = implode('/', $tab_root_map);
  $router_item['tab_parent_href'] = implode('/', $tab_parent_map);
  $router_item['options'] = array();
  _menu_check_access($router_item, $map);

  // For performance, don't localize an item the user can't access.
  if ($router_item['access']) {
    _menu_item_localize($router_item, $map);
  }

  return $map;
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
