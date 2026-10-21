# includes/session.inc

- **Source:** [local](../../../source/includes/session.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/session.inc) · 623 lines

## File documentation

```text
@file
User session handling functions.

The user-level session storage handlers:
- _drupal_session_open()
- _drupal_session_close()
- _drupal_session_read()
- _drupal_session_write()
- _drupal_session_destroy()
- _drupal_session_garbage_collection()
are assigned by session_set_save_handler() in bootstrap.inc and are called
automatically by PHP. These functions should not be called directly. Session
data should instead be accessed via the $_SESSION superglobal.
```

## Functions (derived index)

- [_drupal_session_open()](_drupal_session_open.md) — Session handler assigned by session_set_save_handler().
- [_drupal_session_close()](_drupal_session_close.md) — Session handler assigned by session_set_save_handler().
- [_drupal_session_read()](_drupal_session_read.md) — Reads an entire session from the database (internal use only).
- [_drupal_session_write()](_drupal_session_write.md) — Writes an entire session to the database (internal use only).
- [drupal_session_initialize()](drupal_session_initialize.md) — Initializes the session handler, starting a session if needed.
- [drupal_session_start()](drupal_session_start.md) — Starts a session forcefully, preserving already set session data.
- [drupal_session_commit()](drupal_session_commit.md) — Commits the current session, if necessary.
- [drupal_session_started()](drupal_session_started.md) — Returns whether a session has been started.
- [drupal_session_regenerate()](drupal_session_regenerate.md) — Called when an anonymous user becomes authenticated or vice-versa.
- [_drupal_session_regenerate_existing()](_drupal_session_regenerate_existing.md) — Regenerates an existing session.
- [_drupal_session_destroy()](_drupal_session_destroy.md) — Session handler assigned by session_set_save_handler().
- [_drupal_session_delete_cookie()](_drupal_session_delete_cookie.md) — Deletes the session cookie.
- [drupal_session_destroy_uid()](drupal_session_destroy_uid.md) — Ends a specific user's session(s).
- [_drupal_session_garbage_collection()](_drupal_session_garbage_collection.md) — Session handler assigned by session_set_save_handler().
- [drupal_save_session()](drupal_save_session.md) — Determines whether to save session data of the current request.
- [drupal_session_id()](drupal_session_id.md) — Session ids are hashed by default before being stored in the database.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
