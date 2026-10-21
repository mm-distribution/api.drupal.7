# user_admin_role_delete_submit()

- **Type:** Function
- **File:** [`modules/user/user.admin.inc`](_file.md), lines 1046–1048 · [local source](../../../../source/modules/user/user.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.admin.inc#L1046-L1048)
- **Module/theme:** user

## Signature

```php
function user_admin_role_delete_submit($form, &$form_state)
```

## Documentation

```text
Form submit handler for the user_admin_role() form.
```

## Code

```php
function user_admin_role_delete_submit($form, &$form_state) {
  $form_state['redirect'] = 'admin/people/permissions/roles/delete/' . $form_state['values']['rid'];
}
```

---
_Drupal 7.103 · [modules/user/user.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/user/user.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
