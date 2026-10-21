# profile_field_form_submit()

- **Type:** Function
- **File:** [`modules/profile/profile.admin.inc`](_file.md), lines 363–391 · [local source](../../../../source/modules/profile/profile.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.admin.inc#L363-L391)
- **Module/theme:** profile

## Signature

```php
function profile_field_form_submit($form, &$form_state)
```

## Documentation

```text
Process profile_field_form submissions.
```

## Code

```php
function profile_field_form_submit($form, &$form_state) {
  if (!isset($form_state['values']['options'])) {
    $form_state['values']['options'] = '';
  }
  if (!isset($form_state['values']['page'])) {
    $form_state['values']['page'] = '';
  }
  // Remove all elements that are not profile_field columns.
  $values = array_intersect_key($form_state['values'], array_flip(array('type', 'category', 'title', 'name', 'explanation', 'visibility', 'page', 'weight', 'autocomplete', 'required', 'register', 'options')));
  if (!isset($form_state['values']['fid'])) {
    db_insert('profile_field')
      ->fields($values)
      ->execute();
    drupal_set_message(t('The field has been created.'));
    watchdog('profile', 'Profile field %field added under category %category.', array('%field' => $form_state['values']['title'], '%category' => $form_state['values']['category']), WATCHDOG_NOTICE, l(t('view'), 'admin/config/people/profile'));
  }
  else {
    db_update('profile_field')
      ->fields($values)
      ->condition('fid', $form_state['values']['fid'])
      ->execute();
    drupal_set_message(t('The field has been updated.'));
  }
  cache_clear_all();
  menu_rebuild();

  $form_state['redirect'] = 'admin/config/people/profile';
  return;
}
```

---
_Drupal 7.103 · [modules/profile/profile.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
