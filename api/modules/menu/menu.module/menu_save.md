# menu_save()

- **Type:** Function
- **File:** [`modules/menu/menu.module`](_file.md), lines 259–287 · [local source](../../../../source/modules/menu/menu.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module#L259-L287)
- **Module/theme:** menu

## Signature

```php
function menu_save($menu)
```

## Documentation

```text
Save a custom menu.

@param $menu
  An array representing a custom menu:
  - menu_name: The unique name of the custom menu (composed of lowercase
    letters, numbers, and hyphens).
  - title: The human readable menu title.
  - description: The custom menu description.

Modules should always pass a fully populated $menu when saving a custom
menu, so other modules are able to output proper status or watchdog messages.

@see menu_load()
```

## Code

```php
function menu_save($menu) {
  $status = db_merge('menu_custom')
    ->key(array('menu_name' => $menu['menu_name']))
    ->fields(array(
      'title' => $menu['title'],
      'description' => $menu['description'],
    ))
    ->execute();
  menu_cache_clear_all();

  switch ($status) {
    case SAVED_NEW:
      // Make sure the menu is present in the active menus variable so that its
      // items may appear in the menu active trail.
      // @see menu_set_active_menu_names()
      $active_menus = variable_get('menu_default_active_menus', array_keys(menu_get_menus()));
      if (!in_array($menu['menu_name'], $active_menus)) {
        $active_menus[] = $menu['menu_name'];
        variable_set('menu_default_active_menus', $active_menus);
      }

      module_invoke_all('menu_insert', $menu);
      break;

    case SAVED_UPDATED:
      module_invoke_all('menu_update', $menu);
      break;
  }
}
```

---
_Drupal 7.103 · [modules/menu/menu.module](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module) · Licensed GPL-2.0-or-later (see LICENSE)._
