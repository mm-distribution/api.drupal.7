# drupal_session_initialize()

- **Type:** Function
- **File:** [`includes/session.inc`](_file.md), lines 242–277 · [local source](../../../source/includes/session.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/session.inc#L242-L277)

## Signature

```php
function drupal_session_initialize()
```

## Documentation

```text
Initializes the session handler, starting a session if needed.
```

## Code

```php
function drupal_session_initialize() {
  global $user, $is_https;

  session_set_save_handler('_drupal_session_open', '_drupal_session_close', '_drupal_session_read', '_drupal_session_write', '_drupal_session_destroy', '_drupal_session_garbage_collection');

  // We use !empty() in the following check to ensure that blank session IDs
  // are not valid.
  if (!empty($_COOKIE[session_name()]) || ($is_https && variable_get('https', FALSE) && !empty($_COOKIE[substr(session_name(), 1)]))) {
    // If a session cookie exists, initialize the session. Otherwise the
    // session is only started on demand in drupal_session_commit(), making
    // anonymous users not use a session cookie unless something is stored in
    // $_SESSION. This allows HTTP proxies to cache anonymous pageviews.
    drupal_session_start();
    if (!empty($user->uid) || !empty($_SESSION)) {
      drupal_page_is_cacheable(FALSE);
    }
  }
  else {
    // Set a session identifier for this request. This is necessary because
    // we lazily start sessions at the end of this request, and some
    // processes (like drupal_get_token()) needs to know the future
    // session ID in advance.
    $GLOBALS['lazy_session'] = TRUE;
    $user = drupal_anonymous_user();
    // Less random sessions (which are much faster to generate) are used for
    // anonymous users than are generated in drupal_session_regenerate() when
    // a user becomes authenticated.
    session_id(drupal_random_key());
    if ($is_https && variable_get('https', FALSE)) {
      $insecure_session_name = substr(session_name(), 1);
      $session_id = drupal_random_key();
      $_COOKIE[$insecure_session_name] = $session_id;
    }
  }
  date_default_timezone_set(drupal_get_user_timezone());
}
```

---
_Drupal 7.103 · [includes/session.inc](https://github.com/drupal/drupal/blob/7.103/includes/session.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
