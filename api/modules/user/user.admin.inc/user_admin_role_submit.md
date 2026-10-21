# user_admin_role_submit()

- **Type:** Function
- **File:** [`modules/user/user.admin.inc`](_file.md), lines 1029–1041 · [local source](../../../../source/modules/user/user.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.admin.inc#L1029-L1041)
- **Module/theme:** user

## Signature

```php
function user_admin_role_submit($form, &$form_state)
```

## Documentation

```text
Form submit handler for the user_admin_role() form.
```

## Code

```php
function user_admin_role_submit($form, &$form_state) {
  $role = (object) $form_state['values'];
  if ($form_state['values']['op'] == t('Save role')) {
    user_role_save($role);
    drupal_set_message(t('The role has been renamed.'));
  }
  elseif ($form_state['values']['op'] == t('Add role')) {
    user_role_save($role);
    drupal_set_message(t('The role has been added.'));
  }
  $form_state['redirect'] = 'admin/people/permissions/roles';
  return;
}
```

---
_Drupal 7.103 · [modules/user/user.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/user/user.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
