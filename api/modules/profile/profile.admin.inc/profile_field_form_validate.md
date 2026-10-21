# profile_field_form_validate()

- **Type:** Function
- **File:** [`modules/profile/profile.admin.inc`](_file.md), lines 310–358 · [local source](../../../../source/modules/profile/profile.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.admin.inc#L310-L358)
- **Module/theme:** profile

## Signature

```php
function profile_field_form_validate($form, &$form_state)
```

## Documentation

```text
Validate profile_field_form submissions.
```

## Code

```php
function profile_field_form_validate($form, &$form_state) {
  // Validate the 'field name':
  if (preg_match('/[^a-zA-Z0-9_-]/', $form_state['values']['name'])) {
    form_set_error('name', t('The specified form name contains one or more illegal characters. Spaces or any other special characters except dash (-) and underscore (_) are not allowed.'));
  }

  $users_table = drupal_get_schema('users');
  if (!empty($users_table['fields'][$form_state['values']['name']])) {
    form_set_error('name', t('The specified form name is reserved for use by Drupal.'));
  }
  // Validate the category:
  if (!$form_state['values']['category']) {
    form_set_error('category', t('You must enter a category.'));
  }
  if (strtolower($form_state['values']['category']) == 'account') {
    form_set_error('category', t('The specified category name is reserved for use by Drupal.'));
  }
  $query = db_select('profile_field');
  $query->fields('profile_field', array('fid'));

  if (isset($form_state['values']['fid'])) {
    $query->condition('fid', $form_state['values']['fid'], '<>');
  }
  $query_name = clone $query;

  $title = $query
    ->condition('title', $form_state['values']['title'])
    ->condition('category', $form_state['values']['category'])
    ->execute()
    ->fetchField();
  if ($title) {
    form_set_error('title', t('The specified title is already in use.'));
  }
  $name = $query_name
    ->condition('name', $form_state['values']['name'])
    ->execute()
    ->fetchField();
  if ($name) {
    form_set_error('name', t('The specified name is already in use.'));
  }
  if ($form_state['values']['visibility'] == PROFILE_HIDDEN) {
    if ($form_state['values']['required']) {
      form_set_error('required', t('A hidden field cannot be required.'));
    }
    if ($form_state['values']['register']) {
      form_set_error('register', t('A hidden field cannot be set to visible on the user registration form.'));
    }
  }
}
```

---
_Drupal 7.103 · [modules/profile/profile.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
