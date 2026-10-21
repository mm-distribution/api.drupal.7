# menu_custom_delete_submit()

- **Type:** Function
- **File:** [`modules/menu/menu.admin.inc`](_file.md), lines 524–526 · [local source](../../../../source/modules/menu/menu.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc#L524-L526)
- **Module/theme:** menu

## Signature

```php
function menu_custom_delete_submit($form, &$form_state)
```

## Documentation

```text
Submit function for the 'Delete' button on the menu editing form.
```

## Code

```php
function menu_custom_delete_submit($form, &$form_state) {
  $form_state['redirect'] = 'admin/structure/menu/manage/' . $form_state['values']['menu_name'] . '/delete';
}
```

---
_Drupal 7.103 · [modules/menu/menu.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
