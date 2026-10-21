# menu_load()

- **Type:** Function
- **File:** [`modules/menu/menu.module`](_file.md), lines 219–222 · [local source](../../../../source/modules/menu/menu.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module#L219-L222)
- **Module/theme:** menu

## Signature

```php
function menu_load($menu_name)
```

## Documentation

```text
Load the data for a single custom menu.

@param $menu_name
  The unique name of a custom menu to load.
@return
  Array defining the custom menu, or FALSE if the menu doesn't exist.
```

## Code

```php
function menu_load($menu_name) {
  $all_menus = menu_load_all();
  return isset($all_menus[$menu_name]) ? $all_menus[$menu_name] : FALSE;
}
```

---
_Drupal 7.103 · [modules/menu/menu.module](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module) · Licensed GPL-2.0-or-later (see LICENSE)._
