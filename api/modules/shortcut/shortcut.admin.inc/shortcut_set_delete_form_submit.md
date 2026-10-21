# shortcut_set_delete_form_submit()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.admin.inc`](_file.md), lines 712–717 · [local source](../../../../source/modules/shortcut/shortcut.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc#L712-L717)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_set_delete_form_submit($form, &$form_state)
```

## Documentation

```text
Submit handler for shortcut_set_delete_form().
```

## Code

```php
function shortcut_set_delete_form_submit($form, &$form_state) {
  $shortcut_set = shortcut_set_load($form_state['values']['shortcut_set']);
  shortcut_set_delete($shortcut_set);
  $form_state['redirect'] = 'admin/config/user-interface/shortcut';
  drupal_set_message(t('The shortcut set %title has been deleted.', array('%title' => $shortcut_set->title)));
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
