# menu_item_delete_page()

- **Type:** Function
- **File:** [`modules/menu/menu.admin.inc`](_file.md), lines 640–647 · [local source](../../../../source/modules/menu/menu.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc#L640-L647)
- **Module/theme:** menu

## Signature

```php
function menu_item_delete_page($item)
```

## Documentation

```text
Menu callback; Check access and present a confirm form for deleting a menu link.
```

## Code

```php
function menu_item_delete_page($item) {
  // Links defined via hook_menu may not be deleted. Updated items are an
  // exception, as they can be broken.
  if ($item['module'] == 'system' && !$item['updated']) {
    return MENU_ACCESS_DENIED;
  }
  return drupal_get_form('menu_item_delete_form', $item);
}
```

---
_Drupal 7.103 · [modules/menu/menu.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
