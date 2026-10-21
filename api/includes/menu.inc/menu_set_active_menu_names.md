# menu_set_active_menu_names()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 2335–2345 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L2335-L2345)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_set_active_menu_names($menu_names = NULL)
```

## Documentation

```text
Sets (or gets) the active menu for the current page.

The active menu for the page determines the active trail.

@return
  An array of menu machine names, in order of preference. The
  'menu_default_active_menus' variable may be used to assert a menu order
  different from the order of creation, or to prevent a particular menu from
  being used at all in the active trail.
  E.g., $conf['menu_default_active_menus'] = array('navigation', 'main-menu')
```

## Code

```php
function menu_set_active_menu_names($menu_names = NULL) {
  $active = &drupal_static(__FUNCTION__);

  if (isset($menu_names) && is_array($menu_names)) {
    $active = $menu_names;
  }
  elseif (!isset($active)) {
    $active = variable_get('menu_default_active_menus', array_keys(menu_list_system_menus()));
  }
  return $active;
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
