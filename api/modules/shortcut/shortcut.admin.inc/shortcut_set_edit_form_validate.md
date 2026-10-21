# shortcut_set_edit_form_validate()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.admin.inc`](_file.md), lines 637–643 · [local source](../../../../source/modules/shortcut/shortcut.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc#L637-L643)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_set_edit_form_validate($form, &$form_state)
```

## Documentation

```text
Validation handler for shortcut_set_edit_form().
```

## Code

```php
function shortcut_set_edit_form_validate($form, &$form_state) {
  // Check to prevent a duplicate title, if the title was edited from its
  // original value.
  if ($form_state['values']['title'] != $form_state['values']['shortcut_set']->title && shortcut_set_title_exists($form_state['values']['title'])) {
    form_set_error('title', t('The shortcut set %name already exists. Choose another name.', array('%name' => $form_state['values']['title'])));
  }
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
