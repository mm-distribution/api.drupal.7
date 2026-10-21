# _menu_link_translate()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 881–954 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L881-L954)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function _menu_link_translate(&$item, $translate = FALSE)
```

## Documentation

```text
Provides menu link access control, translation, and argument handling.

This function is similar to _menu_translate(), but it also does
link-specific preparation (such as always calling to_arg() functions).

@param $item
  A menu link.
@param $translate
  (optional) Whether to try to translate a link containing dynamic path
  argument placeholders (%) based on the menu router item of the current
  path. Defaults to FALSE. Internally used for breadcrumbs.

@return
  Returns the map of path arguments with objects loaded as defined in the
  $item['load_functions'].
  $item['access'] becomes TRUE if the item is accessible, FALSE otherwise.
  $item['href'] is generated from link_path, possibly by to_arg functions.
  $item['title'] is generated from link_title, and may be localized.
  $item['options'] is unserialized; it is also changed within the call here
  to $item['localized_options'] by _menu_item_localize().
```

## Code

```php
function _menu_link_translate(&$item, $translate = FALSE) {
  if (!is_array($item['options'])) {
    $item['options'] = unserialize($item['options']);
  }
  if ($item['external']) {
    $item['access'] = 1;
    $map = array();
    $item['href'] = $item['link_path'];
    $item['title'] = $item['link_title'];
    $item['localized_options'] = $item['options'];
  }
  else {
    // Complete the path of the menu link with elements from the current path,
    // if it contains dynamic placeholders (%).
    $map = explode('/', $item['link_path']);
    if (strpos($item['link_path'], '%') !== FALSE) {
      // Invoke registered to_arg callbacks.
      if (!empty($item['to_arg_functions'])) {
        _menu_link_map_translate($map, $item['to_arg_functions']);
      }
      // Or try to derive the path argument map from the current router item,
      // if this $item's path is within the router item's path. This means
      // that if we are on the current path 'foo/%/bar/%/baz', then
      // menu_get_item() will have translated the menu router item for the
      // current path, and we can take over the argument map for a link like
      // 'foo/%/bar'. This inheritance is only valid for breadcrumb links.
      // @see _menu_tree_check_access()
      // @see menu_get_active_breadcrumb()
      elseif ($translate && ($current_router_item = menu_get_item())) {
        // If $translate is TRUE, then this link is in the active trail.
        // Only translate paths within the current path.
        if (strpos($current_router_item['path'], $item['link_path']) === 0) {
          $count = count($map);
          $map = array_slice($current_router_item['original_map'], 0, $count);
          $item['original_map'] = $map;
          if (isset($current_router_item['map'])) {
            $item['map'] = array_slice($current_router_item['map'], 0, $count);
          }
          // Reset access to check it (for the first time).
          unset($item['access']);
        }
      }
    }
    $item['href'] = implode('/', $map);

    // Skip links containing untranslated arguments.
    if (strpos($item['href'], '%') !== FALSE) {
      $item['access'] = FALSE;
      return FALSE;
    }
    // menu_tree_check_access() may set this ahead of time for links to nodes.
    if (!isset($item['access'])) {
      if (!empty($item['load_functions']) && !_menu_load_objects($item, $map)) {
        // An error occurred loading an object.
        $item['access'] = FALSE;
        return FALSE;
      }
      _menu_check_access($item, $map);
    }
    // For performance, don't localize a link the user can't access.
    if ($item['access']) {
      _menu_item_localize($item, $map, TRUE);
    }
  }

  // Allow other customizations - e.g. adding a page-specific query string to the
  // options array. For performance reasons we only invoke this hook if the link
  // has the 'alter' flag set in the options array.
  if (!empty($item['options']['alter'])) {
    drupal_alter('translated_menu_link', $item, $map);
  }

  return $map;
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
