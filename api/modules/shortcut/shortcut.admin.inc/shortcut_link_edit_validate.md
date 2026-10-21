# shortcut_link_edit_validate()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.admin.inc`](_file.md), lines 512–516 · [local source](../../../../source/modules/shortcut/shortcut.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc#L512-L516)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_link_edit_validate($form, &$form_state)
```

## Documentation

```text
Validation handler for the shortcut link add and edit forms.
```

## Code

```php
function shortcut_link_edit_validate($form, &$form_state) {
  if (!shortcut_valid_link($form_state['values']['shortcut_link']['link_path'])) {
    form_set_error('shortcut_link][link_path', t('The link must correspond to a valid path on the site.'));
  }
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
