# shortcut_set_switch_validate()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.admin.inc`](_file.md), lines 109–120 · [local source](../../../../source/modules/shortcut/shortcut.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc#L109-L120)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_set_switch_validate($form, &$form_state)
```

## Documentation

```text
Validation handler for shortcut_set_switch().
```

## Code

```php
function shortcut_set_switch_validate($form, &$form_state) {
  if ($form_state['values']['set'] == 'new') {
    // Check to prevent creating a shortcut set with an empty title.
    if (trim($form_state['values']['new']) == '') {
      form_set_error('new', t('The new set name is required.'));
    }
    // Check to prevent a duplicate title.
    if (shortcut_set_title_exists($form_state['values']['new'])) {
      form_set_error('new', t('The shortcut set %name already exists. Choose another name.', array('%name' => $form_state['values']['new'])));
    }
  }
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
