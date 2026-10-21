# menu_parent_options_js()

- **Type:** Function
- **File:** [`modules/menu/menu.module`](_file.md), lines 388–398 · [local source](../../../../source/modules/menu/menu.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module#L388-L398)
- **Module/theme:** menu

## Signature

```php
function menu_parent_options_js()
```

## Documentation

```text
Page callback.
Get all the available menus and menu items as a JavaScript array.
```

## Code

```php
function menu_parent_options_js() {
  $available_menus = array();
  if (isset($_POST['menus']) && count($_POST['menus'])) {
    foreach ($_POST['menus'] as $menu) {
      $available_menus[$menu] = $menu;
    }
  }
  $options = _menu_get_options(menu_get_menus(), $available_menus, array('mlid' => 0));

  drupal_json_output($options);
}
```

---
_Drupal 7.103 · [modules/menu/menu.module](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module) · Licensed GPL-2.0-or-later (see LICENSE)._
