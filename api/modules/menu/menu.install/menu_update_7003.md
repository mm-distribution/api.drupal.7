# menu_update_7003()

- **Type:** Function
- **File:** [`modules/menu/menu.install`](_file.md), lines 188–205 · [local source](../../../../source/modules/menu/menu.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.install#L188-L205)
- **Module/theme:** menu
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function menu_update_7003(&$sandbox)
```

## Documentation

```text
Add missing custom menus to active menus list.
```

## Code

```php
function menu_update_7003(&$sandbox) {
  // Make sure all custom menus are present in the active menus variable so that
  // their items may appear in the active trail.
  // @see menu_set_active_menu_names()
  $active_menus = variable_get('menu_default_active_menus', array_keys(menu_list_system_menus()));
  $update_variable = FALSE;
  foreach (menu_get_names() as $menu_name) {
    if (!in_array($menu_name, $active_menus) && (strpos($menu_name, 'menu-') === 0)) {
      $active_menus[] = $menu_name;
      $update_variable = TRUE;
    }
  }
  if ($update_variable) {
    variable_set('menu_default_active_menus', $active_menus);
  }
  // Clear the menu cache.
  cache_clear_all(NULL, 'cache_menu');
}
```

---
_Drupal 7.103 · [modules/menu/menu.install](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.install) · Licensed GPL-2.0-or-later (see LICENSE)._
