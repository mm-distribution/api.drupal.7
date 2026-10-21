# shortcut_link_add_submit()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.admin.inc`](_file.md), lines 539–548 · [local source](../../../../source/modules/shortcut/shortcut.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc#L539-L548)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_link_add_submit($form, &$form_state)
```

## Documentation

```text
Submit handler for shortcut_link_add().
```

## Code

```php
function shortcut_link_add_submit($form, &$form_state) {
  // Add the shortcut link to the set.
  $shortcut_set = $form_state['values']['shortcut_set'];
  $shortcut_link = $form_state['values']['shortcut_link'];
  $shortcut_link['menu_name'] = $shortcut_set->set_name;
  shortcut_admin_add_link($shortcut_link, $shortcut_set, shortcut_max_slots());
  shortcut_set_save($shortcut_set);
  $form_state['redirect'] = 'admin/config/user-interface/shortcut/' . $shortcut_link['menu_name'];
  drupal_set_message(t('Added a shortcut for %title.', array('%title' => $shortcut_link['link_title'])));
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
