# profile_field_delete_submit()

- **Type:** Function
- **File:** [`modules/profile/profile.admin.inc`](_file.md), lines 414–429 · [local source](../../../../source/modules/profile/profile.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.admin.inc#L414-L429)
- **Module/theme:** profile

## Signature

```php
function profile_field_delete_submit($form, &$form_state)
```

## Documentation

```text
Process a field delete form submission.
```

## Code

```php
function profile_field_delete_submit($form, &$form_state) {
  db_delete('profile_field')
    ->condition('fid', $form_state['values']['fid'])
    ->execute();
  db_delete('profile_value')
    ->condition('fid', $form_state['values']['fid'])
    ->execute();

  cache_clear_all();

  drupal_set_message(t('The field %field has been deleted.', array('%field' => $form_state['values']['title'])));
  watchdog('profile', 'Profile field %field deleted.', array('%field' => $form_state['values']['title']), WATCHDOG_NOTICE, l(t('view'), 'admin/config/people/profile'));

  $form_state['redirect'] = 'admin/config/people/profile';
  return;
}
```

---
_Drupal 7.103 · [modules/profile/profile.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
