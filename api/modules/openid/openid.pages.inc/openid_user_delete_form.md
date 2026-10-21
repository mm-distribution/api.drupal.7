# openid_user_delete_form()

- **Type:** Function
- **File:** [`modules/openid/openid.pages.inc`](_file.md), lines 97–104 · [local source](../../../../source/modules/openid/openid.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.pages.inc#L97-L104)
- **Module/theme:** openid

## Signature

```php
function openid_user_delete_form($form, $form_state, $account, $aid = 0)
```

## Documentation

```text
Menu callback; Delete the specified OpenID identity from the system.
```

## Code

```php
function openid_user_delete_form($form, $form_state, $account, $aid = 0) {
  $authname = db_query("SELECT authname FROM {authmap} WHERE uid = :uid AND aid = :aid AND module = 'openid'", array(
    ':uid' => $account->uid,
    ':aid' => $aid,
  ))
  ->fetchField();
  return confirm_form(array(), t('Are you sure you want to delete the OpenID %authname for %user?', array('%authname' => $authname, '%user' => $account->name)), 'user/' . $account->uid . '/openid');
}
```

---
_Drupal 7.103 · [modules/openid/openid.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
