# _openid_invalid_openid_transition()

- **Type:** Function
- **File:** [`modules/openid/openid.inc`](_file.md), lines 843–900 · [local source](../../../../source/modules/openid/openid.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc#L843-L900)
- **Module/theme:** openid

## Signature

```php
function _openid_invalid_openid_transition($identity, $response)
```

## Documentation

```text
Provides transition for accounts with possibly invalid OpenID identifiers in authmap.

This function provides a less safe but more unobtrusive procedure for users
who cannot login with their OpenID identifiers. OpenID identifiers in the
authmap could be incomplete due to invalid OpenID implementation in previous
versions of Drupal (e.g. fragment part of the identifier could be missing).
For more information see http://drupal.org/node/1120290.

@param string $identity
  The user's claimed OpenID identifier.

@return
  A fully-loaded user object if the user is found or FALSE if not found.
```

## Code

```php
function _openid_invalid_openid_transition($identity, $response) {
  $account = FALSE;
  $fallback_account = NULL;
  $fallback_identity = $identity;

  // Try to strip the fragment if it is present.
  if (strpos($fallback_identity, '#') !== FALSE) {
    $fallback_identity = preg_replace('/#.*/', '', $fallback_identity);
    $fallback_account = user_external_load($fallback_identity);
  }

  // Try to replace HTTPS with HTTP. OpenID providers often redirect
  // from http to https, but Drupal didn't follow the redirect.
  if (!$fallback_account && strpos($fallback_identity, 'https://') !== FALSE) {
    $fallback_identity = str_replace('https://', 'http://', $fallback_identity);
    $fallback_account = user_external_load($fallback_identity);
  }

  // Try to use original identifier.
  if (!$fallback_account && isset($_SESSION['openid']['user_login_values']['openid_identifier'])) {
    $fallback_identity = openid_normalize($_SESSION['openid']['user_login_values']['openid_identifier']);
    $fallback_account = user_external_load($fallback_identity);
  }

  if ($fallback_account) {
    // Try to extract e-mail address from Simple Registration (SREG) or
    // Attribute Exchanges (AX) keys.
    $email = '';
    $sreg_values = openid_extract_namespace($response, OPENID_NS_SREG, 'sreg', TRUE);
    $ax_values = openid_extract_namespace($response, OPENID_NS_AX, 'ax', TRUE);
    if (!empty($sreg_values['email']) && valid_email_address($sreg_values['email'])) {
      $email = $sreg_values['email'];
    }
    elseif ($ax_mail_values = openid_extract_ax_values($ax_values, array('http://axschema.org/contact/email', 'http://schema.openid.net/contact/email'))) {
      $email = current($ax_mail_values);
    }

    // If this e-mail address is the same as the e-mail address found in user
    // account, login the user and update the claimed identifier.
    if ($email && ($email == $fallback_account->mail || $email == $fallback_account->init)) {
      $query = db_insert('authmap')
        ->fields(array(
          'authname' => $identity,
          'uid' => $fallback_account->uid,
          'module' => 'openid',
        ))
        ->execute();
      drupal_set_message(t('New OpenID identifier %identity was added as a replacement for invalid identifier %invalid_identity. To finish the invalid OpenID transition process, please go to your <a href="@openid_url">OpenID identities page</a> and remove the old identifier %invalid_identity.', array('%invalid_identity' => $fallback_identity, '%identity' => $identity, '@openid_url' => 'user/' . $fallback_account->uid . '/openid')));
      // Set the account to the found one.
      $account = $fallback_account;
    }
    else {
      drupal_set_message(t('There is already an existing account associated with the OpenID identifier that you have provided. However, due to a bug in the previous version of the authentication system, we can\'t be sure that this account belongs to you. If you are new on this site, please continue registering the new user account. If you already have a registered account on this site associated with the provided OpenID identifier, please try to <a href="@url_password">reset the password</a> or contact the site administrator.', array('@url_password' => 'user/password')), 'warning');
    }
  }

  return $account;
}
```

---
_Drupal 7.103 · [modules/openid/openid.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
