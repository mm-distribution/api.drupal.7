# menu_get_item()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 455–497 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L455-L497)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_get_item($path = NULL, $router_item = NULL)
```

## Documentation

```text
Gets a router item.

@param $path
  The path; for example, 'node/5'. The function will find the corresponding
  node/% item and return that. Defaults to the current path.
@param $router_item
  Internal use only.

@return
  The router item or, if an error occurs in _menu_translate(), FALSE. A
  router item is an associative array corresponding to one row in the
  menu_router table. The value corresponding to the key 'map' holds the
  loaded objects. The value corresponding to the key 'access' is TRUE if the
  current user can access this page. The values corresponding to the keys
  'title', 'page_arguments', 'access_arguments', and 'theme_arguments' will
  be filled in based on the database values and the objects loaded.
```

## Code

```php
function menu_get_item($path = NULL, $router_item = NULL) {
  $router_items = &drupal_static(__FUNCTION__);
  if (!isset($path)) {
    $path = $_GET['q'];
  }
  if (isset($router_item)) {
    $router_items[$path] = $router_item;
  }
  if (!isset($router_items[$path])) {
    // Rebuild if we know it's needed, or if the menu masks are missing which
    // occurs rarely, likely due to a race condition of multiple rebuilds.
    if (variable_get('menu_rebuild_needed', FALSE) || !variable_get('menu_masks', array())) {
      if (_menu_check_rebuild()) {
        menu_rebuild();
      }
    }
    $original_map = arg(NULL, $path);

    $parts = array_slice($original_map, 0, MENU_MAX_PARTS);
    $ancestors = menu_get_ancestors($parts);
    $router_item = db_query_range('SELECT * FROM {menu_router} WHERE path IN (:ancestors) ORDER BY fit DESC', 0, 1, array(':ancestors' => $ancestors))->fetchAssoc();

    if ($router_item) {
      // Allow modules to alter the router item before it is translated and
      // checked for access.
      drupal_alter('menu_get_item', $router_item, $path, $original_map);

      $map = _menu_translate($router_item, $original_map);
      $router_item['original_map'] = $original_map;
      if ($map === FALSE) {
        $router_items[$path] = FALSE;
        return FALSE;
      }
      if ($router_item['access']) {
        $router_item['map'] = $map;
        $router_item['page_arguments'] = array_merge(menu_unserialize($router_item['page_arguments'], $map), array_slice($map, $router_item['number_parts']));
        $router_item['theme_arguments'] = array_merge(menu_unserialize($router_item['theme_arguments'], $map), array_slice($map, $router_item['number_parts']));
      }
    }
    $router_items[$path] = $router_item;
  }
  return $router_items[$path];
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
