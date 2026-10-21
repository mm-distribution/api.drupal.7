# user_admin_roles_order_submit()

- **Type:** Function
- **File:** [`modules/user/user.admin.inc`](_file.md), lines 911–918 · [local source](../../../../source/modules/user/user.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.admin.inc#L911-L918)
- **Module/theme:** user

## Signature

```php
function user_admin_roles_order_submit($form, &$form_state)
```

## Documentation

```text
Form submit function. Update the role weights.
```

## Code

```php
function user_admin_roles_order_submit($form, &$form_state) {
  foreach ($form_state['values']['roles'] as $rid => $role_values) {
    $role = $form['roles'][$rid]['#role'];
    $role->weight = $role_values['weight'];
    user_role_save($role);
  }
  drupal_set_message(t('The role settings have been updated.'));
}
```

---
_Drupal 7.103 · [modules/user/user.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/user/user.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
