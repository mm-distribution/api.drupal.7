# user_admin_role_validate()

- **Type:** Function
- **File:** [`modules/user/user.admin.inc`](_file.md), lines 1007–1024 · [local source](../../../../source/modules/user/user.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.admin.inc#L1007-L1024)
- **Module/theme:** user

## Signature

```php
function user_admin_role_validate($form, &$form_state)
```

## Documentation

```text
Form validation handler for the user_admin_role() form.
```

## Code

```php
function user_admin_role_validate($form, &$form_state) {
  if (!empty($form_state['values']['name'])) {
    if ($form_state['values']['op'] == t('Save role')) {
      $role = user_role_load_by_name($form_state['values']['name']);
      if ($role && $role->rid != $form_state['values']['rid']) {
        form_set_error('name', t('The role name %name already exists. Choose another role name.', array('%name' => $form_state['values']['name'])));
      }
    }
    elseif ($form_state['values']['op'] == t('Add role')) {
      if (user_role_load_by_name($form_state['values']['name'])) {
        form_set_error('name', t('The role name %name already exists. Choose another role name.', array('%name' => $form_state['values']['name'])));
      }
    }
  }
  else {
    form_set_error('name', t('You must specify a valid role name.'));
  }
}
```

---
_Drupal 7.103 · [modules/user/user.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/user/user.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
