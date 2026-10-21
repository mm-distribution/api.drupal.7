# openid_user_identities()

- **Type:** Function
- **File:** [`modules/openid/openid.pages.inc`](_file.md), lines 29–63 · [local source](../../../../source/modules/openid/openid.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.pages.inc#L29-L63)
- **Module/theme:** openid

## Signature

```php
function openid_user_identities($account)
```

## Documentation

```text
Menu callback; Manage OpenID identities for the specified user.
```

## Code

```php
function openid_user_identities($account) {
  drupal_set_title(format_username($account));
  drupal_add_css(drupal_get_path('module', 'openid') . '/openid.css');

  // Check to see if we got a response
  $result = openid_complete();
  if ($result['status'] == 'success') {
    $identity = $result['openid.claimed_id'];
    $query = db_insert('authmap')
      ->fields(array(
        'uid' => $account->uid,
        'authname' => $identity,
        'module' => 'openid',
      ))
      ->execute();
    drupal_set_message(t('Successfully added %identity', array('%identity' => $identity)));
  }

  $header = array(t('OpenID'), t('Operations'));
  $rows = array();

  $result = db_query("SELECT * FROM {authmap} WHERE module='openid' AND uid=:uid", array(':uid' => $account->uid));
  foreach ($result as $identity) {
    $rows[] = array(check_plain($identity->authname), l(t('Delete'), 'user/' . $account->uid . '/openid/delete/' . $identity->aid));
  }

  $build['openid_table'] = array(
    '#theme' => 'table',
    '#header' => $header,
    '#rows' => $rows,
    '#empty' => t('No OpenID identities available for this account.'),
  );
  $build['openid_user_add'] = drupal_get_form('openid_user_add');
  return $build;
}
```

---
_Drupal 7.103 · [modules/openid/openid.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
