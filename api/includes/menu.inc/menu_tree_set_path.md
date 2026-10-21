# menu_tree_set_path()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 1181–1187 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L1181-L1187)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_tree_set_path($menu_name, $path = NULL)
```

## Documentation

```text
Sets the path for determining the active trail of the specified menu tree.

This path will also affect the breadcrumbs under some circumstances.
Breadcrumbs are built using the preferred link returned by
menu_link_get_preferred(). If the preferred link is inside one of the menus
specified in calls to menu_tree_set_path(), the preferred link will be
overridden by the corresponding path returned by menu_tree_get_path().

Setting this path does not affect the main content; for that use
menu_set_active_item() instead.

@param $menu_name
  The name of the affected menu tree.
@param $path
  The path to use when finding the active trail.
```

## Code

```php
function menu_tree_set_path($menu_name, $path = NULL) {
  $paths = &drupal_static(__FUNCTION__);
  if (isset($path)) {
    $paths[$menu_name] = $path;
  }
  return isset($paths[$menu_name]) ? $paths[$menu_name] : NULL;
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
