# user_login_name_validate()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 2171–2176 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L2171-L2176)
- **Module/theme:** user

## Signature

```php
function user_login_name_validate($form, &$form_state)
```

## Documentation

```text
A FAPI validate handler. Sets an error if supplied username has been blocked.
```

## Code

```php
function user_login_name_validate($form, &$form_state) {
  if (!empty($form_state['values']['name']) && user_is_blocked($form_state['values']['name'])) {
    // Blocked in user administration.
    form_set_error('name', t('The username %name has not been activated or is blocked.', array('%name' => $form_state['values']['name'])));
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
