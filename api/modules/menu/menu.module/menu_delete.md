# menu_delete()

- **Type:** Function
- **File:** [`modules/menu/menu.module`](_file.md), lines 313–333 · [local source](../../../../source/modules/menu/menu.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module#L313-L333)
- **Module/theme:** menu

## Signature

```php
function menu_delete($menu)
```

## Documentation

```text
Delete a custom menu and all contained links.

Note that this function deletes all menu links in a custom menu. While menu
links derived from router paths may be restored by rebuilding the menu, all
customized and custom links will be irreversibly gone. Therefore, this
function should usually be called from a user interface (form submit) handler
only, which allows the user to confirm the action.

@param $menu
  An array representing a custom menu:
  - menu_name: The unique name of the custom menu.
  - title: The human readable menu title.
  - description: The custom menu description.

Modules should always pass a fully populated $menu when deleting a custom
menu, so other modules are able to output proper status or watchdog messages.

@see menu_load()

menu_delete_links() will take care of clearing the page cache. Other modules
should take care of their menu-related data by implementing
hook_menu_delete().
```

## Code

```php
function menu_delete($menu) {
  // Delete all links from the menu.
  menu_delete_links($menu['menu_name']);

  // Remove menu from active menus variable.
  $active_menus = variable_get('menu_default_active_menus', array_keys(menu_get_menus()));
  foreach ($active_menus as $i => $menu_name) {
    if ($menu['menu_name'] == $menu_name) {
      unset($active_menus[$i]);
      variable_set('menu_default_active_menus', $active_menus);
    }
  }

  // Delete the custom menu.
  db_delete('menu_custom')
    ->condition('menu_name', $menu['menu_name'])
    ->execute();

  menu_cache_clear_all();
  module_invoke_all('menu_delete', $menu);
}
```

---
_Drupal 7.103 · [modules/menu/menu.module](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module) · Licensed GPL-2.0-or-later (see LICENSE)._
