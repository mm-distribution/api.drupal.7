# user_admin_role_delete_confirm()

- **Type:** Function
- **File:** [`modules/user/user.admin.inc`](_file.md), lines 1053–1059 · [local source](../../../../source/modules/user/user.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.admin.inc#L1053-L1059)
- **Module/theme:** user

## Signature

```php
function user_admin_role_delete_confirm($form, &$form_state, $role)
```

## Documentation

```text
Form to confirm role delete operation.
```

## Code

```php
function user_admin_role_delete_confirm($form, &$form_state, $role) {
  $form['rid'] = array(
    '#type' => 'value',
    '#value' => $role->rid,
  );
  return confirm_form($form, t('Are you sure you want to delete the role %name ?', array('%name' => $role->name)), 'admin/people/permissions/roles', t('This action cannot be undone.'), t('Delete'));
}
```

---
_Drupal 7.103 · [modules/user/user.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/user/user.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
