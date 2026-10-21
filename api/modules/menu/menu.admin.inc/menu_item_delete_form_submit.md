# menu_item_delete_form_submit()

- **Type:** Function
- **File:** [`modules/menu/menu.admin.inc`](_file.md), lines 660–667 · [local source](../../../../source/modules/menu/menu.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc#L660-L667)
- **Module/theme:** menu

## Signature

```php
function menu_item_delete_form_submit($form, &$form_state)
```

## Documentation

```text
Process menu delete form submissions.
```

## Code

```php
function menu_item_delete_form_submit($form, &$form_state) {
  $item = $form['#item'];
  menu_link_delete($item['mlid']);
  $t_args = array('%title' => $item['link_title']);
  drupal_set_message(t('The menu link %title has been deleted.', $t_args));
  watchdog('menu', 'Deleted menu link %title.', $t_args, WATCHDOG_NOTICE);
  $form_state['redirect'] = 'admin/structure/menu/manage/' . $item['menu_name'];
}
```

---
_Drupal 7.103 · [modules/menu/menu.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
