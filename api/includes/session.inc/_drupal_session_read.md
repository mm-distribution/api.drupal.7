# _drupal_session_read()

- **Type:** Function
- **File:** [`includes/session.inc`](_file.md), lines 70–140 · [local source](../../../source/includes/session.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/session.inc#L70-L140)

## Signature

```php
function _drupal_session_read($sid)
```

## Documentation

```text
Reads an entire session from the database (internal use only).

Also initializes the $user object for the user associated with the session.
This function is registered with session_set_save_handler() to support
database-backed sessions. It is called on every page load when PHP sets
up the $_SESSION superglobal.

This function is an internal function and must not be called directly.
Doing so may result in logging out the current user, corrupting session data
or other unexpected behavior. Session data must always be accessed via the
$_SESSION superglobal.

@param $sid
  The session ID of the session to retrieve.

@return
  The user's session, or an empty string if no session exists.
```

## Code

```php
function _drupal_session_read($sid) {
  global $user, $is_https;

  // Write and Close handlers are called after destructing objects
  // since PHP 5.0.5.
  // Thus destructors can use sessions but session handler can't use objects.
  // So we are moving session closure before destructing objects.
  drupal_register_shutdown_function('session_write_close');

  // Handle the case of first time visitors and clients that don't store
  // cookies (eg. web crawlers).
  $insecure_session_name = substr(session_name(), 1);
  if (empty($sid) || (!isset($_COOKIE[session_name()]) && !isset($_COOKIE[$insecure_session_name]))) {
    $user = drupal_anonymous_user();
    return '';
  }

  // Otherwise, if the session is still active, we have a record of the
  // client's session in the database. If it's HTTPS then we are either have
  // a HTTPS session or we are about to log in so we check the sessions table
  // for an anonymous session with the non-HTTPS-only cookie. The session ID
  // that is in the user's cookie is hashed before being stored in the database
  // as a security measure. Thus, we have to hash it to match the database.
  if ($is_https) {
    $user = db_query("SELECT u.*, s.* FROM {users} u INNER JOIN {sessions} s ON u.uid = s.uid WHERE s.ssid = :ssid", array(':ssid' => drupal_session_id($sid)))->fetchObject();
    if (!$user) {
      if (isset($_COOKIE[$insecure_session_name])) {
        $user = db_query("SELECT u.*, s.* FROM {users} u INNER JOIN {sessions} s ON u.uid = s.uid WHERE s.sid = :sid AND s.uid = 0", array(
        ':sid' => drupal_session_id($_COOKIE[$insecure_session_name])))
        ->fetchObject();
      }
    }
  }
  else {
    $user = db_query("SELECT u.*, s.* FROM {users} u INNER JOIN {sessions} s ON u.uid = s.uid WHERE s.sid = :sid", array(':sid' => drupal_session_id($sid)))->fetchObject();
  }

  // We found the client's session record and they are an authenticated,
  // active user.
  if ($user && $user->uid > 0 && $user->status == 1) {
    // This is done to unserialize the data member of $user.
    $user->data = unserialize((string) $user->data);

    // Add roles element to $user.
    $user->roles = array();
    $user->roles[DRUPAL_AUTHENTICATED_RID] = 'authenticated user';
    $user->roles += db_query("SELECT r.rid, r.name FROM {role} r INNER JOIN {users_roles} ur ON ur.rid = r.rid WHERE ur.uid = :uid", array(':uid' => $user->uid))->fetchAllKeyed(0, 1);
  }
  elseif ($user) {
    // The user is anonymous or blocked. Only preserve two fields from the
    // {sessions} table.
    $account = drupal_anonymous_user();
    $account->session = $user->session;
    $account->timestamp = $user->timestamp;
    $user = $account;
  }
  else {
    // The session has expired.
    $user = drupal_anonymous_user();
    $user->session = '';
  }

  // Store the session that was read for comparison in _drupal_session_write().
  $last_read = &drupal_static('drupal_session_last_read');
  $last_read = array(
    'sid' => $sid,
    'value' => $user->session,
  );

  return $user->session;
}
```

---
_Drupal 7.103 · [includes/session.inc](https://github.com/drupal/drupal/blob/7.103/includes/session.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
