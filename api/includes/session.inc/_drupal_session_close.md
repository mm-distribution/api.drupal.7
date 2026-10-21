# _drupal_session_close()

- **Type:** Function
- **File:** [`includes/session.inc`](_file.md), lines 47–49 · [local source](../../../source/includes/session.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/session.inc#L47-L49)

## Signature

```php
function _drupal_session_close()
```

## Documentation

```text
Session handler assigned by session_set_save_handler().

This function is used to close the current session. Because Drupal stores
session data in the database immediately on write, this function does
not need to do anything.

This function should not be called directly.

@return
  This function will always return TRUE.
```

## Code

```php
function _drupal_session_close() {
  return TRUE;
}
```

---
_Drupal 7.103 · [includes/session.inc](https://github.com/drupal/drupal/blob/7.103/includes/session.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
