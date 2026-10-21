# menu_reset_item_confirm()

- **Type:** Function
- **File:** [`modules/menu/menu.admin.inc`](_file.md), lines 672–675 · [local source](../../../../source/modules/menu/menu.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc#L672-L675)
- **Module/theme:** menu

## Signature

```php
function menu_reset_item_confirm($form, &$form_state, $item)
```

## Documentation

```text
Menu callback; reset a single modified menu link.
```

## Code

```php
function menu_reset_item_confirm($form, &$form_state, $item) {
  $form['item'] = array('#type' => 'value', '#value' => $item);
  return confirm_form($form, t('Are you sure you want to reset the link %item to its default values?', array('%item' => $item['link_title'])), 'admin/structure/menu/manage/' . $item['menu_name'], t('Any customizations will be lost. This action cannot be undone.'), t('Reset'));
}
```

---
_Drupal 7.103 · [modules/menu/menu.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
