# drupal_session_commit()

- **Type:** Function
- **File:** [`includes/session.inc`](_file.md), lines 319–356 · [local source](../../../source/includes/session.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/session.inc#L319-L356)

## Signature

```php
function drupal_session_commit()
```

## Documentation

```text
Commits the current session, if necessary.

If an anonymous user already have an empty session, destroy it.
```

## Code

```php
function drupal_session_commit() {
  global $user, $is_https;

  if (!drupal_save_session()) {
    // We don't have anything to do if we are not allowed to save the session.
    return;
  }

  if (empty($user->uid) && empty($_SESSION)) {
    // There is no session data to store, destroy the session if it was
    // previously started.
    if (drupal_session_started()) {
      session_destroy();
    }
  }
  else {
    // There is session data to store. Start the session if it is not already
    // started.
    if (!drupal_session_started()) {
      drupal_session_start();
      if ($is_https && variable_get('https', FALSE)) {
        $insecure_session_name = substr(session_name(), 1);
        $params = session_get_cookie_params();
        $expire = $params['lifetime'] ? REQUEST_TIME + $params['lifetime'] : 0;
        $options = array(
          'expires' => $expire,
          'path' => $params['path'],
          'domain' => $params['domain'],
          'secure' => FALSE,
          'httponly' => $params['httponly'],
        );
        drupal_setcookie($insecure_session_name, $_COOKIE[$insecure_session_name], $options);
      }
    }
    // Write the session data.
    session_write_close();
  }
}
```

---
_Drupal 7.103 · [includes/session.inc](https://github.com/drupal/drupal/blob/7.103/includes/session.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
