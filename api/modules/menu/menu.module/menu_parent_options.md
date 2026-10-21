# menu_parent_options()

- **Type:** Function
- **File:** [`modules/menu/menu.module`](_file.md), lines 353–382 · [local source](../../../../source/modules/menu/menu.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module#L353-L382)
- **Module/theme:** menu

## Signature

```php
function menu_parent_options($menus, $item, $type = '')
```

## Documentation

```text
Return a list of menu items that are valid possible parents for the given menu item.

@param $menus
  An array of menu names and titles, such as from menu_get_menus().
@param $item
  The menu item or the node type for which to generate a list of parents.
  If $item['mlid'] == 0 then the complete tree is returned.
@param $type
  The node type for which to generate a list of parents.
  If $item itself is a node type then $type is ignored.
@return
  An array of menu link titles keyed on the a string containing the menu name
  and mlid. The list excludes the given item and its children.

@todo This has to be turned into a #process form element callback. The
  'menu_override_parent_selector' variable is entirely superfluous.
```

## Code

```php
function menu_parent_options($menus, $item, $type = '') {
  // The menu_links table can be practically any size and we need a way to
  // allow contrib modules to provide more scalable pattern choosers.
  // hook_form_alter is too late in itself because all the possible parents are
  // retrieved here, unless menu_override_parent_selector is set to TRUE.
  if (variable_get('menu_override_parent_selector', FALSE)) {
    return array();
  }

  $available_menus = array();
  if (!is_array($item)) {
    // If $item is not an array then it is a node type.
    // Use it as $type and prepare a dummy menu item for _menu_get_options().
    $type = $item;
    $item = array('mlid' => 0);
  }
  if (empty($type)) {
    // If no node type is set, use all menus given to this function.
    $available_menus = $menus;
  }
  else {
    // If a node type is set, use all available menus for this type.
    $type_menus = variable_get('menu_options_' . $type, array('main-menu' => 'main-menu'));
    foreach ($type_menus as $menu) {
      $available_menus[$menu] = $menu;
    }
  }

  return _menu_get_options($menus, $available_menus, $item);
}
```

---
_Drupal 7.103 · [modules/menu/menu.module](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module) · Licensed GPL-2.0-or-later (see LICENSE)._
