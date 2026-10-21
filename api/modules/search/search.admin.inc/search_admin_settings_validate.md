# search_admin_settings_validate()

- **Type:** Function
- **File:** [`modules/search/search.admin.inc`](_file.md), lines 155–164 · [local source](../../../../source/modules/search/search.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.admin.inc#L155-L164)
- **Module/theme:** search

## Signature

```php
function search_admin_settings_validate($form, &$form_state)
```

## Documentation

```text
Form validation handler for search_admin_settings().
```

## Code

```php
function search_admin_settings_validate($form, &$form_state) {
  // Check whether we selected a valid default.
  if ($form_state['triggering_element']['#value'] != t('Reset to defaults')) {
    $new_modules = array_filter($form_state['values']['search_active_modules']);
    $default = $form_state['values']['search_default_module'];
    if (!in_array($default, $new_modules, TRUE)) {
      form_set_error('search_default_module', t('Your default search module is not selected as an active module.'));
    }
  }
}
```

---
_Drupal 7.103 · [modules/search/search.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/search/search.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
