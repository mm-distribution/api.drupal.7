# _drupal_session_garbage_collection()

- **Type:** Function
- **File:** [`includes/session.inc`](_file.md), lines 567–577 · [local source](../../../source/includes/session.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/session.inc#L567-L577)

## Signature

```php
function _drupal_session_garbage_collection($lifetime)
```

## Documentation

```text
Session handler assigned by session_set_save_handler().

Cleans up stalled sessions.

@param $lifetime
  The value of session.gc_maxlifetime, passed by PHP.
  Sessions not updated for more than $lifetime seconds will be removed.
```

## Code

```php
function _drupal_session_garbage_collection($lifetime) {
  // Be sure to adjust 'php_value session.gc_maxlifetime' to a large enough
  // value. For example, if you want user sessions to stay in your database
  // for three weeks before deleting them, you need to set gc_maxlifetime
  // to '1814400'. At that value, only after a user doesn't log in after
  // three weeks (1814400 seconds) will his/her session be removed.
  db_delete('sessions')
    ->condition('timestamp', REQUEST_TIME - $lifetime, '<')
    ->execute();
  return TRUE;
}
```

---
_Drupal 7.103 · [includes/session.inc](https://github.com/drupal/drupal/blob/7.103/includes/session.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
