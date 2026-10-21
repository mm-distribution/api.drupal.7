# _user_mail_text()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 2771–2928 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L2771-L2928)
- **Module/theme:** user

## Signature

```php
function _user_mail_text($key, $language = NULL, $variables = array(), $replace = TRUE)
```

## Documentation

```text
Returns a mail string for a variable name.

Used by user_mail() and the settings forms to retrieve strings.
```

## Code

```php
function _user_mail_text($key, $language = NULL, $variables = array(), $replace = TRUE) {
  $langcode = isset($language) ? $language->language : NULL;

  if ($admin_setting = variable_get('user_mail_' . $key, FALSE)) {
    // An admin setting overrides the default string.
    $text = $admin_setting;
  }
  else {
    // No override, return default string.
    switch ($key) {
      case 'register_no_approval_required_subject':
        $text = t('Account details for [user:name] at [site:name]', array(), array('langcode' => $langcode));
        break;
      case 'register_no_approval_required_body':
        $text = t("[user:name],

Thank you for registering at [site:name]. You may now log in by clicking this link or copying and pasting it to your browser:

[user:one-time-login-url]

This link can only be used once to log in and will lead you to a page where you can set your password.

After setting your password, you will be able to log in at [site:login-url] in the future using:

username: [user:name]
password: Your password

--  [site:name] team", array(), array('langcode' => $langcode));
        break;

      case 'register_admin_created_subject':
        $text = t('An administrator created an account for you at [site:name]', array(), array('langcode' => $langcode));
        break;
      case 'register_admin_created_body':
        $text = t("[user:name],

A site administrator at [site:name] has created an account for you. You may now log in by clicking this link or copying and pasting it to your browser:

[user:one-time-login-url]

This link can only be used once to log in and will lead you to a page where you can set your password.

After setting your password, you will be able to log in at [site:login-url] in the future using:

username: [user:name]
password: Your password

--  [site:name] team", array(), array('langcode' => $langcode));
        break;

      case 'register_pending_approval_subject':
      case 'register_pending_approval_admin_subject':
        $text = t('Account details for [user:name] at [site:name] (pending admin approval)', array(), array('langcode' => $langcode));
        break;
      case 'register_pending_approval_body':
        $text = t("[user:name],

Thank you for registering at [site:name]. Your application for an account is currently pending approval. Once it has been approved, you will receive another e-mail containing information about how to log in, set your password, and other details.


--  [site:name] team", array(), array('langcode' => $langcode));
        break;
      case 'register_pending_approval_admin_body':
        $text = t("[user:name] has applied for an account.

[user:edit-url]", array(), array('langcode' => $langcode));
        break;

      case 'password_reset_subject':
        $text = t('Replacement login information for [user:name] at [site:name]', array(), array('langcode' => $langcode));
        break;
      case 'password_reset_body':
        $text = t("[user:name],

A request to reset the password for your account has been made at [site:name].

You may now log in by clicking this link or copying and pasting it to your browser:

[user:one-time-login-url]

This link can only be used once to log in and will lead you to a page where you can set your password. It expires after one day and nothing will happen if it's not used.

--  [site:name] team", array(), array('langcode' => $langcode));
        break;

      case 'status_activated_subject':
        $text = t('Account details for [user:name] at [site:name] (approved)', array(), array('langcode' => $langcode));
        break;
      case 'status_activated_body':
        $text = t("[user:name],

Your account at [site:name] has been activated.

You may now log in by clicking this link or copying and pasting it into your browser:

[user:one-time-login-url]

This link can only be used once to log in and will lead you to a page where you can set your password.

After setting your password, you will be able to log in at [site:login-url] in the future using:

username: [user:name]
password: Your password

--  [site:name] team", array(), array('langcode' => $langcode));
        break;

      case 'status_blocked_subject':
        $text = t('Account details for [user:name] at [site:name] (blocked)', array(), array('langcode' => $langcode));
        break;
      case 'status_blocked_body':
        $text = t("[user:name],

Your account on [site:name] has been blocked.

--  [site:name] team", array(), array('langcode' => $langcode));
        break;

      case 'cancel_confirm_subject':
        $text = t('Account cancellation request for [user:name] at [site:name]', array(), array('langcode' => $langcode));
        break;
      case 'cancel_confirm_body':
        $text = t("[user:name],

A request to cancel your account has been made at [site:name].

You may now cancel your account on [site:url-brief] by clicking this link or copying and pasting it into your browser:

[user:cancel-url]

NOTE: The cancellation of your account is not reversible.

This link expires in one day and nothing will happen if it is not used.

--  [site:name] team", array(), array('langcode' => $langcode));
        break;

      case 'status_canceled_subject':
        $text = t('Account details for [user:name] at [site:name] (canceled)', array(), array('langcode' => $langcode));
        break;
      case 'status_canceled_body':
        $text = t("[user:name],

Your account on [site:name] has been canceled.

--  [site:name] team", array(), array('langcode' => $langcode));
        break;
    }
  }

  if ($replace) {
    // We do not sanitize the token replacement, since the output of this
    // replacement is intended for an e-mail message, not a web browser.
    return token_replace($text, $variables, array('language' => $language, 'callback' => 'user_mail_tokens', 'sanitize' => FALSE, 'clear' => TRUE));
  }

  return $text;
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
