# user_admin_role_delete_confirm_submit()

- **Type:** Function
- **File:** [`modules/user/user.admin.inc`](_file.md), lines 1064–1068 · [local source](../../../../source/modules/user/user.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.admin.inc#L1064-L1068)
- **Module/theme:** user

## Signature

```php
function user_admin_role_delete_confirm_submit($form, &$form_state)
```

## Documentation

```text
Form submit handler for user_admin_role_delete_confirm().
```

## Code

```php
function user_admin_role_delete_confirm_submit($form, &$form_state) {
  user_role_delete((int) $form_state['values']['rid']);
  drupal_set_message(t('The role has been deleted.'));
  $form_state['redirect'] = 'admin/people/permissions/roles';
}
```

---
_Drupal 7.103 · [modules/user/user.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/user/user.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
