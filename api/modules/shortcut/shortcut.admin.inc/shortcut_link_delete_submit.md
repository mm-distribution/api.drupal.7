# shortcut_link_delete_submit()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.admin.inc`](_file.md), lines 754–759 · [local source](../../../../source/modules/shortcut/shortcut.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc#L754-L759)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_link_delete_submit($form, &$form_state)
```

## Documentation

```text
Submit handler for shortcut_link_delete_submit().
```

## Code

```php
function shortcut_link_delete_submit($form, &$form_state) {
  $shortcut_link = $form_state['values']['shortcut_link'];
  menu_link_delete($shortcut_link['mlid']);
  $form_state['redirect'] = 'admin/config/user-interface/shortcut/' . $shortcut_link['menu_name'];
  drupal_set_message(t('The shortcut %title has been deleted.', array('%title' => $shortcut_link['link_title'])));
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
