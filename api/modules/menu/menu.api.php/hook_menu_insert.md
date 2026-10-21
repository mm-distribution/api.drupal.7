# hook_menu_insert()

- **Type:** Hook (documentation function)
- **File:** [`modules/menu/menu.api.php`](_file.md), lines 29–34 · [local source](../../../../source/modules/menu/menu.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.api.php#L29-L34)
- **Module/theme:** menu
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_menu_insert($menu)
```

## Documentation

```text
Respond to a custom menu creation.

This hook is used to notify modules that a custom menu has been created.
Contributed modules may use the information to perform actions based on the
information entered into the menu system.

@param $menu
  An array representing a custom menu:
  - menu_name: The unique name of the custom menu.
  - title: The human readable menu title.
  - description: The custom menu description.

@see hook_menu_update()
@see hook_menu_delete()
```

## Code

```php
function hook_menu_insert($menu) {
  // For example, we track available menus in a variable.
  $my_menus = variable_get('my_module_menus', array());
  $my_menus[$menu['menu_name']] = $menu['menu_name'];
  variable_set('my_module_menus', $my_menus);
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_menu_insert()".

_None found._

---
_Drupal 7.103 · [modules/menu/menu.api.php](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
