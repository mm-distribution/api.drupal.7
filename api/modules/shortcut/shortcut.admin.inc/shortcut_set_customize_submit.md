# shortcut_set_customize_submit()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.admin.inc`](_file.md), lines 318–328 · [local source](../../../../source/modules/shortcut/shortcut.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc#L318-L328)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_set_customize_submit($form, &$form_state)
```

## Documentation

```text
Submit handler for shortcut_set_customize().
```

## Code

```php
function shortcut_set_customize_submit($form, &$form_state) {
  foreach ($form_state['values']['shortcuts'] as $group => $links) {
    foreach ($links as $mlid => $data) {
      $link = menu_link_load($mlid);
      $link['hidden'] = $data['status'] == 'enabled' ? 0 : 1;
      $link['weight'] = $data['weight'];
      menu_link_save($link);
    }
  }
  drupal_set_message(t('The shortcut set has been updated.'));
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
