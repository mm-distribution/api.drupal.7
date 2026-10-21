# _lock_id()

- **Type:** Function
- **File:** [`includes/lock.inc`](_file.md), lines 95–108 · [local source](../../../source/includes/lock.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/lock.inc#L95-L108)
- **Topics:** [lock](../../topics/lock.md)

## Signature

```php
function _lock_id()
```

## Documentation

```text
Helper function to get this request's unique id.
```

## Code

```php
function _lock_id() {
  // Do not use drupal_static(). This identifier refers to the current
  // client request, and must not be changed under any circumstances
  // else the shutdown handler may fail to release our locks.
  static $lock_id;

  if (!isset($lock_id)) {
    // Assign a unique id.
    $lock_id = uniqid(mt_rand(), TRUE);
    // We only register a shutdown function if a lock is used.
    drupal_register_shutdown_function('lock_release_all', $lock_id);
  }
  return $lock_id;
}
```

---
_Drupal 7.103 · [includes/lock.inc](https://github.com/drupal/drupal/blob/7.103/includes/lock.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
