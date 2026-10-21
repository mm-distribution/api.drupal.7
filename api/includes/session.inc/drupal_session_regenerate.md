# drupal_session_regenerate()

- **Type:** Function
- **File:** [`includes/session.inc`](_file.md), lines 374–454 · [local source](../../../source/includes/session.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/session.inc#L374-L454)
- **Topics:** [php_wrappers](../../topics/php_wrappers.md)

## Signature

```php
function drupal_session_regenerate()
```

## Documentation

```text
Called when an anonymous user becomes authenticated or vice-versa.

@ingroup php_wrappers
```

## Code

```php
function drupal_session_regenerate() {
  global $user, $is_https;
  // Nothing to do if we are not allowed to change the session.
  if (!drupal_save_session()) {
    return;
  }

  if ($is_https && variable_get('https', FALSE)) {
    $insecure_session_name = substr(session_name(), 1);
    if (!isset($GLOBALS['lazy_session']) && isset($_COOKIE[$insecure_session_name])) {
      $old_insecure_session_id = $_COOKIE[$insecure_session_name];
    }
    $params = session_get_cookie_params();
    $session_id = drupal_random_key();
    // If a session cookie lifetime is set, the session will expire
    // $params['lifetime'] seconds from the current request. If it is not set,
    // it will expire when the browser is closed.
    $expire = $params['lifetime'] ? REQUEST_TIME + $params['lifetime'] : 0;
    $options = array(
      'expires' => $expire,
      'path' => $params['path'],
      'domain' => $params['domain'],
      'secure' => FALSE,
      'httponly' => $params['httponly'],
    );
    drupal_setcookie($insecure_session_name, $session_id, $options);
    $_COOKIE[$insecure_session_name] = $session_id;
  }

  if (drupal_session_started()) {
    $old_session_id = session_id();
    _drupal_session_regenerate_existing();
  }
  else {
    session_id(drupal_random_key());
  }

  if (isset($old_session_id)) {
    $params = session_get_cookie_params();
    $expire = $params['lifetime'] ? REQUEST_TIME + $params['lifetime'] : 0;
    $options = array(
      'expires' => $expire,
      'path' => $params['path'],
      'domain' => $params['domain'],
      'secure' => $params['secure'],
      'httponly' => $params['httponly'],
    );
    drupal_setcookie(session_name(), session_id(), $options);
    $fields = array('sid' => drupal_session_id(session_id()));
    if ($is_https) {
      $fields['ssid'] = drupal_session_id(session_id());
      // If the "secure pages" setting is enabled, use the newly-created
      // insecure session identifier as the regenerated sid.
      if (variable_get('https', FALSE)) {
        $fields['sid'] = drupal_session_id($session_id);
      }
    }
    db_update('sessions')
      ->fields($fields)
      ->condition($is_https ? 'ssid' : 'sid', drupal_session_id($old_session_id))
      ->execute();
  }
  elseif (isset($old_insecure_session_id)) {
    // If logging in to the secure site, and there was no active session on the
    // secure site but a session was active on the insecure site, update the
    // insecure session with the new session identifiers.
    db_update('sessions')
      ->fields(array('sid' => drupal_session_id($session_id), 'ssid' => drupal_session_id(session_id())))
      ->condition('sid', drupal_session_id($old_insecure_session_id))
      ->execute();
  }
  else {
    // Start the session when it doesn't exist yet.
    // Preserve the logged in user, as it will be reset to anonymous
    // by _drupal_session_read.
    $account = $user;
    drupal_session_start();
    $user = $account;
  }
  date_default_timezone_set(drupal_get_user_timezone());
}
```

---
_Drupal 7.103 · [includes/session.inc](https://github.com/drupal/drupal/blob/7.103/includes/session.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
