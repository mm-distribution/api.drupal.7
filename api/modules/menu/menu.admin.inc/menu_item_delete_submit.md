# menu_item_delete_submit()

- **Type:** Function
- **File:** [`modules/menu/menu.admin.inc`](_file.md), lines 429–431 · [local source](../../../../source/modules/menu/menu.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc#L429-L431)
- **Module/theme:** menu

## Signature

```php
function menu_item_delete_submit($form, &$form_state)
```

## Documentation

```text
Submit function for the delete button on the menu item editing form.
```

## Code

```php
function menu_item_delete_submit($form, &$form_state) {
  $form_state['redirect'] = 'admin/structure/menu/item/' . $form_state['values']['mlid'] . '/delete';
}
```

---
_Drupal 7.103 · [modules/menu/menu.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
