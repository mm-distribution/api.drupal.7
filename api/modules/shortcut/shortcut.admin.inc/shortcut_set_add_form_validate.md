# shortcut_set_add_form_validate()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.admin.inc`](_file.md), lines 228–233 · [local source](../../../../source/modules/shortcut/shortcut.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc#L228-L233)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_set_add_form_validate($form, &$form_state)
```

## Documentation

```text
Validation handler for shortcut_set_add_form().
```

## Code

```php
function shortcut_set_add_form_validate($form, &$form_state) {
  // Check to prevent a duplicate title.
  if (shortcut_set_title_exists($form_state['values']['new'])) {
    form_set_error('new', t('The shortcut set %name already exists. Choose another name.', array('%name' => $form_state['values']['new'])));
  }
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
