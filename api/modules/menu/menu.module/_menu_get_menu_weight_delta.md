# _menu_get_menu_weight_delta()

- **Type:** Function
- **File:** [`modules/menu/menu.module`](_file.md), lines 654–674 · [local source](../../../../source/modules/menu/menu.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module#L654-L674)
- **Module/theme:** menu

## Signature

```php
function _menu_get_menu_weight_delta($menu_names, $max_delta = NULL)
```

## Documentation

```text
Calculate the delta for the weight element for a given set of menus.

@param string|array $menu_names
  Menu name or an array of menu names.
@param int $max_delta
  Optional maximum value.

@return int
  Delta value.
```

## Code

```php
function _menu_get_menu_weight_delta($menu_names, $max_delta = NULL) {

  if (is_string($menu_names)) {
    $menu_names = array($menu_names);
  }

  $weight_info = db_query("SELECT MAX(weight) AS max_weight, MIN(weight) as min_weight FROM {menu_links} WHERE menu_name IN (:menu_names)", array(':menu_names' => $menu_names))->fetchObject();

  $delta = max(abs((int) $weight_info->min_weight), abs((int) $weight_info->max_weight)) + 1;

  // Honor max param, if given.
  if (!is_null($max_delta) && $delta > $max_delta) {
    $delta = $max_delta;
  }

  // Provide a minimum.
  if ($delta < 50) {
    $delta = 50;
  }
  return $delta;
}
```

---
_Drupal 7.103 · [modules/menu/menu.module](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module) · Licensed GPL-2.0-or-later (see LICENSE)._
