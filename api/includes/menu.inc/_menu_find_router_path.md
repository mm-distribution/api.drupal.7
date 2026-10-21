# _menu_find_router_path()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 3426–3456 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L3426-L3456)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function _menu_find_router_path($link_path)
```

## Documentation

```text
Finds the router path which will serve this path.

@param $link_path
 The path for we are looking up its router path.

@return
 A path from $menu keys or empty if $link_path points to a nonexisting
 place.
```

## Code

```php
function _menu_find_router_path($link_path) {
  // $menu will only have data during a menu rebuild.
  $menu = _menu_router_cache();

  $router_path = $link_path;
  $parts = explode('/', $link_path, MENU_MAX_PARTS);
  $ancestors = menu_get_ancestors($parts);

  if (empty($menu)) {
    // Not during a menu rebuild, so look up in the database.
    $router_path = (string) db_select('menu_router')
      ->fields('menu_router', array('path'))
      ->condition('path', $ancestors, 'IN')
      ->orderBy('fit', 'DESC')
      ->range(0, 1)
      ->execute()->fetchField();
  }
  elseif (!isset($menu[$router_path])) {
    // Add an empty router path as a fallback.
    $ancestors[] = '';
    foreach ($ancestors as $key => $router_path) {
      if (isset($menu[$router_path])) {
        // Exit the loop leaving $router_path as the first match.
        break;
      }
    }
    // If we did not find the path, $router_path will be the empty string
    // at the end of $ancestors.
  }
  return $router_path;
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
