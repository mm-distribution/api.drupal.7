# _drupal_session_write()

- **Type:** Function
- **File:** [`includes/session.inc`](_file.md), lines 160–237 · [local source](../../../source/includes/session.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/session.inc#L160-L237)

## Signature

```php
function _drupal_session_write($sid, $value)
```

## Documentation

```text
Writes an entire session to the database (internal use only).

This function is registered with session_set_save_handler() to support
database-backed sessions.

This function is an internal function and must not be called directly.
Doing so may result in corrupted session data or other unexpected behavior.
Session data must always be accessed via the $_SESSION superglobal.

@param $sid
  The session ID of the session to write to.
@param $value
  Session data to write as a serialized string.

@return
  Always returns TRUE.
```

## Code

```php
function _drupal_session_write($sid, $value) {
  global $user, $is_https;

  // The exception handler is not active at this point, so we need to do it
  // manually.
  try {
    if (!drupal_save_session()) {
      // We don't have anything to do if we are not allowed to save the session.
      return TRUE;
    }

    // Check whether $_SESSION has been changed in this request.
    $last_read = &drupal_static('drupal_session_last_read');
    $is_changed = !isset($last_read) || $last_read['sid'] != $sid || $last_read['value'] !== $value;

    // For performance reasons, do not update the sessions table, unless
    // $_SESSION has changed or more than 180 has passed since the last update.
    if ($is_changed || !isset($user->timestamp) || REQUEST_TIME - $user->timestamp > variable_get('session_write_interval', 180)) {
      // Either ssid or sid or both will be added from $key below.
      $fields = array(
        'uid' => $user->uid,
        'cache' => isset($user->cache) ? $user->cache : 0,
        'hostname' => ip_address(),
        'session' => $value,
        'timestamp' => REQUEST_TIME,
      );

      // Use the session ID as 'sid' and an empty string as 'ssid' by default.
      // _drupal_session_read() does not allow empty strings so that's a safe
      // default.
      $key = array('sid' => drupal_session_id($sid), 'ssid' => '');
      // On HTTPS connections, use the session ID as both 'sid' and 'ssid'.
      if ($is_https) {
        $key['ssid'] = drupal_session_id($sid);
        // The "secure pages" setting allows a site to simultaneously use both
        // secure and insecure session cookies. If enabled and both cookies are
        // presented then use both keys. The session ID from the cookie is
        // hashed before being stored in the database as a security measure.
        if (variable_get('https', FALSE)) {
          $insecure_session_name = substr(session_name(), 1);
          if (isset($_COOKIE[$insecure_session_name])) {
            $key['sid'] = drupal_session_id($_COOKIE[$insecure_session_name]);
          }
        }
      }
      elseif (variable_get('https', FALSE)) {
        unset($key['ssid']);
      }

      db_merge('sessions')
        ->key($key)
        ->fields($fields)
        ->execute();
    }

    // Likewise, do not update access time more than once per 180 seconds.
    if ($user->uid && REQUEST_TIME - $user->access > variable_get('session_write_interval', 180)) {
      db_update('users')
        ->fields(array(
          'access' => REQUEST_TIME
        ))
        ->condition('uid', $user->uid)
        ->execute();
    }

    return TRUE;
  }
  catch (Exception $exception) {
    require_once DRUPAL_ROOT . '/includes/errors.inc';
    // If we are displaying errors, then do so with no possibility of a further
    // uncaught exception being thrown.
    if (error_displayable()) {
      print '<h1>Uncaught exception thrown in session handler.</h1>';
      print '<p>' . _drupal_render_exception_safe($exception) . '</p><hr />';
    }
    return FALSE;
  }
}
```

---
_Drupal 7.103 · [includes/session.inc](https://github.com/drupal/drupal/blob/7.103/includes/session.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
