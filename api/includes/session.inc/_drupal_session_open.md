# _drupal_session_open()

- **Type:** Function
- **File:** [`includes/session.inc`](_file.md), lines 31–33 · [local source](../../../source/includes/session.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/session.inc#L31-L33)

## Signature

```php
function _drupal_session_open()
```

## Documentation

```text
Session handler assigned by session_set_save_handler().

This function is used to handle any initialization, such as file paths or
database connections, that is needed before accessing session data. Drupal
does not need to initialize anything in this function.

This function should not be called directly.

@return
  This function will always return TRUE.
```

## Code

```php
function _drupal_session_open() {
  return TRUE;
}
```

---
_Drupal 7.103 · [includes/session.inc](https://github.com/drupal/drupal/blob/7.103/includes/session.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
