# menu_delete_menu_confirm_submit()

- **Type:** Function
- **File:** [`modules/menu/menu.admin.inc`](_file.md), lines 557–585 · [local source](../../../../source/modules/menu/menu.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc#L557-L585)
- **Module/theme:** menu

## Signature

```php
function menu_delete_menu_confirm_submit($form, &$form_state)
```

## Documentation

```text
Delete a custom menu and all links in it.
```

## Code

```php
function menu_delete_menu_confirm_submit($form, &$form_state) {
  $menu = $form['#menu'];
  $form_state['redirect'] = 'admin/structure/menu';

  // System-defined menus may not be deleted - only menus defined by this module.
  $system_menus = menu_list_system_menus();
  if (isset($system_menus[$menu['menu_name']])  || !(db_query("SELECT 1 FROM {menu_custom} WHERE menu_name = :menu", array(':menu' => $menu['menu_name']))->fetchField())) {
    return;
  }

  // Reset all the menu links defined by the system via hook_menu().
  $result = db_query("SELECT * FROM {menu_links} ml INNER JOIN {menu_router} m ON ml.router_path = m.path WHERE ml.menu_name = :menu AND ml.module = 'system' ORDER BY m.number_parts ASC", array(':menu' => $menu['menu_name']), array('fetch' => PDO::FETCH_ASSOC));
  foreach ($result as $link) {
    menu_reset_item($link);
  }

  // Delete all links to the overview page for this menu.
  $result = db_query("SELECT mlid FROM {menu_links} ml WHERE ml.link_path = :link", array(':link' => 'admin/structure/menu/manage/' . $menu['menu_name']), array('fetch' => PDO::FETCH_ASSOC));
  foreach ($result as $link) {
    menu_link_delete($link['mlid']);
  }

  // Delete the custom menu and all its menu links.
  menu_delete($menu);

  $t_args = array('%title' => $menu['title']);
  drupal_set_message(t('The custom menu %title has been deleted.', $t_args));
  watchdog('menu', 'Deleted custom menu %title and all its menu links.', $t_args, WATCHDOG_NOTICE);
}
```

---
_Drupal 7.103 · [modules/menu/menu.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
