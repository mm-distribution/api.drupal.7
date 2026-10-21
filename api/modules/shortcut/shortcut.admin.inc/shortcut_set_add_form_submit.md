# shortcut_set_add_form_submit()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.admin.inc`](_file.md), lines 238–248 · [local source](../../../../source/modules/shortcut/shortcut.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc#L238-L248)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_set_add_form_submit($form, &$form_state)
```

## Documentation

```text
Submit handler for shortcut_set_add_form().
```

## Code

```php
function shortcut_set_add_form_submit($form, &$form_state) {
  // Save a new shortcut set with links copied from the user's default set.
  $default_set = shortcut_default_set();
  $set = (object) array(
    'title' => $form_state['values']['new'],
    'links' => menu_links_clone($default_set->links),
  );
  shortcut_set_save($set);
  drupal_set_message(t('The %set_name shortcut set has been created. You can edit it from this page.', array('%set_name' => $set->title)));
  $form_state['redirect'] = 'admin/config/user-interface/shortcut/' . $set->set_name;
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
