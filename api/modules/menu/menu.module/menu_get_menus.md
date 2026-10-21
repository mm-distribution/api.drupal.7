# menu_get_menus()

- **Type:** Function
- **File:** [`modules/menu/menu.module`](_file.md), lines 853–864 · [local source](../../../../source/modules/menu/menu.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module#L853-L864)
- **Module/theme:** menu

## Signature

```php
function menu_get_menus($all = TRUE)
```

## Documentation

```text
Return an associative array of the custom menus names.

@param $all
  If FALSE return only user-added menus, or if TRUE also include
  the menus defined by the system.
@return
  An array with the machine-readable names as the keys, and human-readable
  titles as the values.
```

## Code

```php
function menu_get_menus($all = TRUE) {
  if ($custom_menus = menu_load_all()) {
    if (!$all) {
      $custom_menus = array_diff_key($custom_menus, menu_list_system_menus());
    }
    foreach ($custom_menus as $menu_name => $menu) {
      $custom_menus[$menu_name] = t($menu['title']);
    }
    asort($custom_menus);
  }
  return $custom_menus;
}
```

---
_Drupal 7.103 · [modules/menu/menu.module](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module) · Licensed GPL-2.0-or-later (see LICENSE)._
