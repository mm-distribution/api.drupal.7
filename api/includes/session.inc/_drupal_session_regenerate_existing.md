# _drupal_session_regenerate_existing()

- **Type:** Function
- **File:** [`includes/session.inc`](_file.md), lines 459–474 · [local source](../../../source/includes/session.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/session.inc#L459-L474)

## Signature

```php
function _drupal_session_regenerate_existing()
```

## Documentation

```text
Regenerates an existing session.
```

## Code

```php
function _drupal_session_regenerate_existing() {
  global $user;
  // Preserve existing settings for the saving of sessions.
  $original_save_session_status = drupal_save_session();
  // Turn off saving of sessions.
  drupal_save_session(FALSE);
  session_write_close();
  drupal_session_started(FALSE);
  // Preserve the user object, as starting a new session will reset it.
  $original_user = $user;
  session_id(drupal_random_key());
  drupal_session_start();
  $user = $original_user;
  // Restore the original settings for the saving of sessions.
  drupal_save_session($original_save_session_status);
}
```

---
_Drupal 7.103 · [includes/session.inc](https://github.com/drupal/drupal/blob/7.103/includes/session.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
