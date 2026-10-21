# menu_load_all()

- **Type:** Function
- **File:** [`modules/menu/menu.module`](_file.md), lines 230–242 · [local source](../../../../source/modules/menu/menu.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module#L230-L242)
- **Module/theme:** menu

## Signature

```php
function menu_load_all()
```

## Documentation

```text
Load all custom menu data.

@return
  Array of custom menu data.
```

## Code

```php
function menu_load_all() {
  $custom_menus = &drupal_static(__FUNCTION__);
  if (!isset($custom_menus)) {
    if ($cached = cache_get('menu_custom', 'cache_menu')) {
      $custom_menus = $cached->data;
    }
    else {
      $custom_menus = db_query('SELECT * FROM {menu_custom}')->fetchAllAssoc('menu_name', PDO::FETCH_ASSOC);
      cache_set('menu_custom', $custom_menus, 'cache_menu');
    }
  }
  return $custom_menus;
}
```

---
_Drupal 7.103 · [modules/menu/menu.module](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module) · Licensed GPL-2.0-or-later (see LICENSE)._
