# shortcut_set_edit_form_submit()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.admin.inc`](_file.md), lines 648–654 · [local source](../../../../source/modules/shortcut/shortcut.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc#L648-L654)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_set_edit_form_submit($form, &$form_state)
```

## Documentation

```text
Submit handler for shortcut_set_edit_form().
```

## Code

```php
function shortcut_set_edit_form_submit($form, &$form_state) {
  $shortcut_set = $form_state['values']['shortcut_set'];
  $shortcut_set->title = $form_state['values']['title'];
  shortcut_set_save($shortcut_set);
  drupal_set_message(t('Updated set name to %set-name.', array('%set-name' => $shortcut_set->title)));
  $form_state['redirect'] = "admin/config/user-interface/shortcut/$shortcut_set->set_name";
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
