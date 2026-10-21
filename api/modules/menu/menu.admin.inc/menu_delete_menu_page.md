# menu_delete_menu_page()

- **Type:** Function
- **File:** [`modules/menu/menu.admin.inc`](_file.md), lines 531–538 · [local source](../../../../source/modules/menu/menu.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc#L531-L538)
- **Module/theme:** menu

## Signature

```php
function menu_delete_menu_page($menu)
```

## Documentation

```text
Menu callback; check access and get a confirm form for deletion of a custom menu.
```

## Code

```php
function menu_delete_menu_page($menu) {
  // System-defined menus may not be deleted.
  $system_menus = menu_list_system_menus();
  if (isset($system_menus[$menu['menu_name']])) {
    return MENU_ACCESS_DENIED;
  }
  return drupal_get_form('menu_delete_menu_confirm', $menu);
}
```

---
_Drupal 7.103 · [modules/menu/menu.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
