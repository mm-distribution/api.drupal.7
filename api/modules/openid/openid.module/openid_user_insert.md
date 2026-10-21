# openid_user_insert()

- **Type:** Function
- **File:** [`modules/openid/openid.module`](_file.md), lines 86–96 · [local source](../../../../source/modules/openid/openid.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module#L86-L96)
- **Module/theme:** openid
- **Implements:** [hook_user_insert()](../../user/user.api.php/hook_user_insert.md)

## Signature

```php
function openid_user_insert(&$edit, $account, $category)
```

## Documentation

```text
Implements hook_user_insert().
```

## Code

```php
function openid_user_insert(&$edit, $account, $category) {
  if (!empty($edit['openid_claimed_id'])) {
    // The user has registered after trying to log in via OpenID.
    if (variable_get('user_email_verification', TRUE)) {
      drupal_set_message(t('Once you have verified your e-mail address, you may log in via OpenID.'));
    }
    user_set_authmaps($account, array('authname_openid' => $edit['openid_claimed_id']));
    unset($_SESSION['openid']);
    unset($edit['openid_claimed_id']);
  }
}
```

---
_Drupal 7.103 · [modules/openid/openid.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module) · Licensed GPL-2.0-or-later (see LICENSE)._
