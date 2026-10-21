# shortcut_link_edit_submit()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.admin.inc`](_file.md), lines 521–534 · [local source](../../../../source/modules/shortcut/shortcut.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc#L521-L534)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_link_edit_submit($form, &$form_state)
```

## Documentation

```text
Submit handler for shortcut_link_edit().
```

## Code

```php
function shortcut_link_edit_submit($form, &$form_state) {
  // Normalize the path in case it is an alias.
  $shortcut_path = drupal_get_normal_path($form_state['values']['shortcut_link']['link_path']);
  if (empty($shortcut_path)) {
    $shortcut_path = '<front>';
  }
  $form_state['values']['shortcut_link']['link_path'] = $shortcut_path;

  $shortcut_link = array_merge($form_state['values']['original_shortcut_link'], $form_state['values']['shortcut_link']);

  menu_link_save($shortcut_link);
  $form_state['redirect'] = 'admin/config/user-interface/shortcut/' . $shortcut_link['menu_name'];
  drupal_set_message(t('The shortcut %link has been updated.', array('%link' => $shortcut_link['link_title'])));
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
