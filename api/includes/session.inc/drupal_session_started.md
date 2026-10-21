# drupal_session_started()

- **Type:** Function
- **File:** [`includes/session.inc`](_file.md), lines 361–367 · [local source](../../../source/includes/session.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/session.inc#L361-L367)

## Signature

```php
function drupal_session_started($set = NULL)
```

## Documentation

```text
Returns whether a session has been started.
```

## Code

```php
function drupal_session_started($set = NULL) {
  static $session_started = FALSE;
  if (isset($set)) {
    $session_started = $set;
  }
  return $session_started && session_id();
}
```

---
_Drupal 7.103 · [includes/session.inc](https://github.com/drupal/drupal/blob/7.103/includes/session.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
