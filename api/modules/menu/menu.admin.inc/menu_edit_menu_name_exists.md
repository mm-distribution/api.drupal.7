# menu_edit_menu_name_exists()

- **Type:** Function
- **File:** [`modules/menu/menu.admin.inc`](_file.md), lines 593–600 · [local source](../../../../source/modules/menu/menu.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc#L593-L600)
- **Module/theme:** menu

## Signature

```php
function menu_edit_menu_name_exists($value)
```

## Documentation

```text
Returns whether a menu name already exists.

@see menu_edit_menu()
@see form_validate_machine_name()
```

## Code

```php
function menu_edit_menu_name_exists($value) {
  // 'menu-' is added to the menu name to avoid name-space conflicts.
  $value = 'menu-' . $value;
  $custom_exists = db_query_range('SELECT 1 FROM {menu_custom} WHERE menu_name = :menu', 0, 1, array(':menu' => $value))->fetchField();
  $link_exists = db_query_range("SELECT 1 FROM {menu_links} WHERE menu_name = :menu", 0, 1, array(':menu' => $value))->fetchField();

  return $custom_exists || $link_exists;
}
```

---
_Drupal 7.103 · [modules/menu/menu.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
