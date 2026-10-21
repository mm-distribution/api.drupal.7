# _drupal_session_destroy()

- **Type:** Function
- **File:** [`includes/session.inc`](_file.md), lines 484–512 · [local source](../../../source/includes/session.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/session.inc#L484-L512)

## Signature

```php
function _drupal_session_destroy($sid)
```

## Documentation

```text
Session handler assigned by session_set_save_handler().

Cleans up a specific session.

@param $sid
  Session ID.
```

## Code

```php
function _drupal_session_destroy($sid) {
  global $user, $is_https;

  // Nothing to do if we are not allowed to change the session.
  if (!drupal_save_session()) {
    return TRUE;
  }

  // Delete session data.
  db_delete('sessions')
    ->condition($is_https ? 'ssid' : 'sid', drupal_session_id($sid))
    ->execute();

  // Reset $_SESSION and $user to prevent a new session from being started
  // in drupal_session_commit().
  $_SESSION = array();
  $user = drupal_anonymous_user();

  // Unset the session cookies.
  _drupal_session_delete_cookie(session_name());
  if ($is_https) {
    _drupal_session_delete_cookie(substr(session_name(), 1), FALSE);
  }
  elseif (variable_get('https', FALSE)) {
    _drupal_session_delete_cookie('S' . session_name(), TRUE);
  }

  return TRUE;
}
```

---
_Drupal 7.103 · [includes/session.inc](https://github.com/drupal/drupal/blob/7.103/includes/session.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
