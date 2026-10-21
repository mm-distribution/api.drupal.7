# user_pass_reset()

- **Type:** Function
- **File:** [`modules/user/user.pages.inc`](_file.md), lines 146–298 · [local source](../../../../source/modules/user/user.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc#L146-L298)
- **Module/theme:** user

## Signature

```php
function user_pass_reset($form, &$form_state, $uid, $timestamp, $hashed_pass, $action = NULL)
```

## Documentation

```text
Menu callback; process one time login link and redirects to the user page on success.

In order to never disclose password reset hashes via referrer headers or
web browser history, this function always issues a redirect when a valid
password reset hash is in the URL.
```

## Code

```php
function user_pass_reset($form, &$form_state, $uid, $timestamp, $hashed_pass, $action = NULL) {
  global $user;

  // Check for a reset hash in the session. Immediately remove it (to prevent it
  // from being reused, for example if this page is visited again via the
  // browser history) and store it for later use.
  if (isset($_SESSION['pass_reset_hash'])) {
    $session_reset_hash = $_SESSION['pass_reset_hash'];
    unset($_SESSION['pass_reset_hash']);
  }
  else {
    $session_reset_hash = NULL;
  }

  // When processing the one-time login link, we have to make sure that a user
  // isn't already logged in.
  if ($user->uid) {
    // The existing user is already logged in. Log them out and reload the
    // current page so the password reset process can continue.
    if ($user->uid == $uid) {
      // Preserve the current destination (if any) and ensure the redirect goes
      // back to the current page; any custom destination set in
      // hook_user_logout() and intended for regular logouts would not be
      // appropriate here.
      $destination = array();
      if (isset($_GET['destination'])) {
        $destination = drupal_get_destination();
      }
      user_logout_current_user();
      unset($_GET['destination']);
      drupal_goto(current_path(), array('query' => drupal_get_query_parameters() + $destination));
    }
    // A different user is already logged in on the computer.
    else {
      $reset_link_account = user_load($uid);
      $is_valid = FALSE;
      if (!empty($reset_link_account) && $timestamp >= $reset_link_account->login && $timestamp <= REQUEST_TIME) {
        if ($hashed_pass == user_pass_rehash($reset_link_account->pass, $timestamp, $reset_link_account->login, $reset_link_account->uid, $reset_link_account->mail)) {
          $is_valid = TRUE;
        }
        elseif ($session_reset_hash && $session_reset_hash == user_pass_rehash($reset_link_account->pass, $timestamp, $reset_link_account->login, $reset_link_account->uid, $reset_link_account->mail)) {
          $is_valid = TRUE;
        }
      }
      if ($is_valid) {
        drupal_set_message(t('Another user (%other_user) is already logged into the site on this computer, but you tried to use a one-time link for user %resetting_user. Please <a href="!logout">logout</a> and try using the link again.',
          array('%other_user' => $user->name, '%resetting_user' => $reset_link_account->name, '!logout' => url('user/logout'))), 'warning');
      } else {
        // Invalid one-time link specifies an unknown user.
        drupal_set_message(t('The one-time login link you clicked is invalid.'), 'error');
      }
      drupal_goto();
    }
  }
  else {
    // Time out, in seconds, until login URL expires. Defaults to 24 hours =
    // 86400 seconds.
    $timeout = variable_get('user_password_reset_timeout', 86400);
    $current = REQUEST_TIME;
    // Some redundant checks for extra security ?
    $users = user_load_multiple(array($uid), array('status' => '1'));
    if ($timestamp <= $current && $account = reset($users)) {
      // No time out for first time login.
      if ($account->login && $current - $timestamp > $timeout) {
        drupal_set_message(t('You have tried to use a one-time login link that has expired. Please request a new one using the form below.'), 'error');
        drupal_goto('user/password');
      }
      // Validate the reset hash from the URL or from the session.
      $is_valid = FALSE;
      if ($account->uid && $timestamp >= $account->login && $timestamp <= $current) {
        // If the reset hash in the URL is valid, put it in the session and
        // redirect to the same URL but with the hash replaced by an invalid
        // one ("confirm"). This prevents disclosing the hash via referrer
        // headers or web browser history.
        if ($hashed_pass == user_pass_rehash($account->pass, $timestamp, $account->login, $account->uid, $account->mail)) {
          if ($action === 'login') {
            // The 'login' action redirects directly to the user edit form.
            $is_valid = TRUE;
          }
          else {
            $_SESSION['pass_reset_hash'] = $hashed_pass;
            $args = arg();
            foreach ($args as &$arg) {
              if ($arg == $hashed_pass) {
                $arg = 'confirm';
              }
            }
            $path = implode('/', $args);
            drupal_goto($path, array('query' => drupal_get_query_parameters()));
          }
        }
        // If the reset hash from the session is valid, use that.
        elseif ($session_reset_hash && $session_reset_hash == user_pass_rehash($account->pass, $timestamp, $account->login, $account->uid, $account->mail)) {
          $is_valid = TRUE;
        }
      }
      if ($is_valid) {
        // First stage is a confirmation form, then login
        if ($action == 'login') {
          if (variable_get('user_failed_login_identifier_uid_only', FALSE)) {
            // Clear flood events based on the uid only if configured.
            $identifier = $account->uid;
          }
          else {
            // The default identifier is a combination of uid and IP address.
            $identifier = $account->uid . '-' . ip_address();
          }
          // Only clear the user specific flood events. We cannot clear the more
          // broad IP address flood events because that would open a
          // vulnerability where an attacker with a valid account could use that
          // to brute force other accounts.
          flood_clear_event('failed_login_attempt_user', $identifier);

          // Set the new user.
          $user = $account;
          // user_login_finalize() also updates the login timestamp of the
          // user, which invalidates further use of the one-time login link.
          user_login_finalize();
          // Clear any password reset flood events for this user.
          flood_clear_event('pass_reset_user', $account->uid);
          watchdog('user', 'User %name used one-time login link at time %timestamp.', array('%name' => $account->name, '%timestamp' => $timestamp));
          drupal_set_message(t('You have just used your one-time login link. It is no longer necessary to use this link to log in. Please change your password.'));
          // Let the user's password be changed without the current password check.
          $token = drupal_random_key();
          $_SESSION['pass_reset_' . $user->uid] = $token;
          drupal_goto('user/' . $user->uid . '/edit', array('query' => array('pass-reset-token' => $token)));
        }
        else {
          $form['message'] = array('#markup' => t('<p>This is a one-time login for %user_name and will expire on %expiration_date.</p><p>Click on this button to log in to the site and change your password.</p>', array('%user_name' => $account->name, '%expiration_date' => format_date($timestamp + $timeout))));
          $form['help'] = array('#markup' => '<p>' . t('This login can be used only once.') . '</p>');
          $form['actions'] = array('#type' => 'actions');
          $form['actions']['submit'] = array('#type' => 'submit', '#value' => t('Log in'));
          $form['#action'] = url("user/reset/$uid/$timestamp/$session_reset_hash/login");
          // Prevent the browser from storing this page so that the token will
          // not be visible in the form action if the back button is used to
          // revisit this page.
          drupal_add_http_header('Cache-Control', 'no-store');
          return $form;
        }
      }
      else {
        drupal_set_message(t('You have tried to use a one-time login link that has either been used or is no longer valid. Please request a new one using the form below.'), 'error');
        drupal_goto('user/password');
      }
    }
    else {
      // Deny access, no more clues.
      // Everything will be in the watchdog's URL for the administrator to check.
      drupal_access_denied();
      drupal_exit();
    }
  }
}
```

---
_Drupal 7.103 · [modules/user/user.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
