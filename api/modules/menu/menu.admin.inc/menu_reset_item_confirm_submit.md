# menu_reset_item_confirm_submit()

- **Type:** Function
- **File:** [`modules/menu/menu.admin.inc`](_file.md), lines 680–685 · [local source](../../../../source/modules/menu/menu.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc#L680-L685)
- **Module/theme:** menu

## Signature

```php
function menu_reset_item_confirm_submit($form, &$form_state)
```

## Documentation

```text
Process menu reset item form submissions.
```

## Code

```php
function menu_reset_item_confirm_submit($form, &$form_state) {
  $item = $form_state['values']['item'];
  $new_item = menu_reset_item($item);
  drupal_set_message(t('The menu link was reset to its default settings.'));
  $form_state['redirect'] = 'admin/structure/menu/manage/' . $new_item['menu_name'];
}
```

---
_Drupal 7.103 · [modules/menu/menu.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
