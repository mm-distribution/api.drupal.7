# search_admin_settings_submit()

- **Type:** Function
- **File:** [`modules/search/search.admin.inc`](_file.md), lines 169–188 · [local source](../../../../source/modules/search/search.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.admin.inc#L169-L188)
- **Module/theme:** search

## Signature

```php
function search_admin_settings_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for search_admin_settings().
```

## Code

```php
function search_admin_settings_submit($form, &$form_state) {
  // If these settings change, the index needs to be rebuilt.
  if ((variable_get('minimum_word_size', 3) != $form_state['values']['minimum_word_size']) ||
      (variable_get('overlap_cjk', TRUE) != $form_state['values']['overlap_cjk'])) {
    drupal_set_message(t('The index will be rebuilt.'));
    search_reindex();
  }
  $current_modules = variable_get('search_active_modules', array('node', 'user'));
  // Check whether we are resetting the values.
  if ($form_state['triggering_element']['#value'] == t('Reset to defaults')) {
    $new_modules = array('node', 'user');
  }
  else {
    $new_modules = array_filter($form_state['values']['search_active_modules']);
  }
  if (array_diff($current_modules, $new_modules)) {
    drupal_set_message(t('The active search modules have been changed.'));
    variable_set('menu_rebuild_needed', TRUE);
  }
}
```

---
_Drupal 7.103 · [modules/search/search.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/search/search.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
