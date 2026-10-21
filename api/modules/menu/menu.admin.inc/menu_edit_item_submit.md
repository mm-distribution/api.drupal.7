# menu_edit_item_submit()

- **Type:** Function
- **File:** [`modules/menu/menu.admin.inc`](_file.md), lines 436–453 · [local source](../../../../source/modules/menu/menu.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc#L436-L453)
- **Module/theme:** menu

## Signature

```php
function menu_edit_item_submit($form, &$form_state)
```

## Documentation

```text
Process menu and menu item add/edit form submissions.
```

## Code

```php
function menu_edit_item_submit($form, &$form_state) {
  $item = &$form_state['values'];

  // The value of "hidden" is the opposite of the value
  // supplied by the "enabled" checkbox.
  $item['hidden'] = (int) !$item['enabled'];
  unset($item['enabled']);

  $item['options']['attributes']['title'] = $item['description'];
  list($item['menu_name'], $item['plid']) = explode(':', $item['parent']);
  if (!menu_link_save($item)) {
    drupal_set_message(t('There was an error saving the menu link.'), 'error');
  }
  else {
    drupal_set_message(t('Your configuration has been saved.'));
  }
  $form_state['redirect'] = 'admin/structure/menu/manage/' . $item['menu_name'];
}
```

---
_Drupal 7.103 · [modules/menu/menu.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
