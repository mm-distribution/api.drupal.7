# drupal_session_destroy_uid()

- **Type:** Function
- **File:** [`includes/session.inc`](_file.md), lines 547–556 · [local source](../../../source/includes/session.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/session.inc#L547-L556)

## Signature

```php
function drupal_session_destroy_uid($uid)
```

## Documentation

```text
Ends a specific user's session(s).

@param $uid
  User ID.
```

## Code

```php
function drupal_session_destroy_uid($uid) {
  // Nothing to do if we are not allowed to change the session.
  if (!drupal_save_session()) {
    return;
  }

  db_delete('sessions')
    ->condition('uid', $uid)
    ->execute();
}
```

---
_Drupal 7.103 · [includes/session.inc](https://github.com/drupal/drupal/blob/7.103/includes/session.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
