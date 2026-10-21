# lock_may_be_available()

- **Type:** Function
- **File:** [`includes/lock.inc`](_file.md), lines 185–203 · [local source](../../../source/includes/lock.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/lock.inc#L185-L203)
- **Topics:** [lock](../../topics/lock.md)

## Signature

```php
function lock_may_be_available($name)
```

## Documentation

```text
Check if lock acquired by a different process may be available.

If an existing lock has expired, it is removed.

@param $name
  The name of the lock.

@return
  TRUE if there is no lock or it was removed, FALSE otherwise.
```

## Code

```php
function lock_may_be_available($name) {
  $lock = db_query('SELECT expire, value FROM {semaphore} WHERE name = :name', array(':name' => $name))->fetchAssoc();
  if (!$lock) {
    return TRUE;
  }
  $expire = (float) $lock['expire'];
  $now = microtime(TRUE);
  if ($now > $expire) {
    // We check two conditions to prevent a race condition where another
    // request acquired the lock and set a new expire time. We add a small
    // number to $expire to avoid errors with float to string conversion.
    return (bool) db_delete('semaphore')
      ->condition('name', $name)
      ->condition('value', $lock['value'])
      ->condition('expire', 0.0001 + $expire, '<=')
      ->execute();
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [includes/lock.inc](https://github.com/drupal/drupal/blob/7.103/includes/lock.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
