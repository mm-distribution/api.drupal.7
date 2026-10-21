# _menu_get_options()

- **Type:** Function
- **File:** [`modules/menu/menu.module`](_file.md), lines 403–426 · [local source](../../../../source/modules/menu/menu.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module#L403-L426)
- **Module/theme:** menu

## Signature

```php
function _menu_get_options($menus, $available_menus, $item)
```

## Documentation

```text
Helper function to get the items of the given menu.
```

## Code

```php
function _menu_get_options($menus, $available_menus, $item) {
  global $menu_admin;
  $menu_admin = TRUE;

  // If the item has children, there is an added limit to the depth of valid parents.
  if (isset($item['parent_depth_limit'])) {
    $limit = $item['parent_depth_limit'];
  }
  else {
    $limit = _menu_parent_depth_limit($item);
  }

  $options = array();
  foreach ($menus as $menu_name => $title) {
    if (isset($available_menus[$menu_name])) {
      $tree = menu_tree_all_data($menu_name, NULL);
      $options[$menu_name . ':0'] = '<' . $title . '>';
      _menu_parents_recurse($tree, $menu_name, '--', $options, $item['mlid'], $limit);
    }
  }

  $menu_admin = FALSE;
  return $options;
}
```

---
_Drupal 7.103 · [modules/menu/menu.module](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module) · Licensed GPL-2.0-or-later (see LICENSE)._
