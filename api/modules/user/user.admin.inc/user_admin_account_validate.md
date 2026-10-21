# user_admin_account_validate()

- **Type:** Function
- **File:** [`modules/user/user.admin.inc`](_file.md), lines 272–277 · [local source](../../../../source/modules/user/user.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.admin.inc#L272-L277)
- **Module/theme:** user

## Signature

```php
function user_admin_account_validate($form, &$form_state)
```

## Documentation

```text
Form validation handler for the user_admin_account() form.
```

## Code

```php
function user_admin_account_validate($form, &$form_state) {
  $form_state['values']['accounts'] = array_filter($form_state['values']['accounts']);
  if (count($form_state['values']['accounts']) == 0) {
    form_set_error('', t('No users selected.'));
  }
}
```

---
_Drupal 7.103 · [modules/user/user.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/user/user.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
