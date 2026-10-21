# menu_item_delete_form()

- **Type:** Function
- **File:** [`modules/menu/menu.admin.inc`](_file.md), lines 652–655 · [local source](../../../../source/modules/menu/menu.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc#L652-L655)
- **Module/theme:** menu

## Signature

```php
function menu_item_delete_form($form, &$form_state, $item)
```

## Documentation

```text
Build a confirm form for deletion of a single menu link.
```

## Code

```php
function menu_item_delete_form($form, &$form_state, $item) {
  $form['#item'] = $item;
  return confirm_form($form, t('Are you sure you want to delete the custom menu link %item?', array('%item' => $item['link_title'])), 'admin/structure/menu/manage/' . $item['menu_name']);
}
```

---
_Drupal 7.103 · [modules/menu/menu.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
