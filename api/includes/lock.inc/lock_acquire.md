# lock_acquire()

- **Type:** Function
- **File:** [`includes/lock.inc`](_file.md), lines 121–172 · [local source](../../../source/includes/lock.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/lock.inc#L121-L172)
- **Topics:** [lock](../../topics/lock.md)

## Signature

```php
function lock_acquire($name, $timeout = 30.0)
```

## Documentation

```text
Acquire (or renew) a lock, but do not block if it fails.

@param $name
  The name of the lock. Limit of name's length is 255 characters.
@param $timeout
  A number of seconds (float) before the lock expires (minimum of 0.001).

@return
  TRUE if the lock was acquired, FALSE if it failed.
```

## Code

```php
function lock_acquire($name, $timeout = 30.0) {
  global $locks;

  // Insure that the timeout is at least 1 ms.
  $timeout = max($timeout, 0.001);
  $expire = microtime(TRUE) + $timeout;
  if (isset($locks[$name])) {
    // Try to extend the expiration of a lock we already acquired.
    $success = (bool) db_update('semaphore')
      ->fields(array('expire' => $expire))
      ->condition('name', $name)
      ->condition('value', _lock_id())
      ->execute();
    if (!$success) {
      // The lock was broken.
      unset($locks[$name]);
    }
    return $success;
  }
  else {
    // Optimistically try to acquire the lock, then retry once if it fails.
    // The first time through the loop cannot be a retry.
    $retry = FALSE;
    // We always want to do this code at least once.
    do {
      try {
        db_insert('semaphore')
          ->fields(array(
            'name' => $name,
            'value' => _lock_id(),
            'expire' => $expire,
          ))
          ->execute();
        // We track all acquired locks in the global variable.
        $locks[$name] = TRUE;
        // We never need to try again.
        $retry = FALSE;
      }
      catch (PDOException $e) {
        // Suppress the error. If this is our first pass through the loop,
        // then $retry is FALSE. In this case, the insert must have failed
        // meaning some other request acquired the lock but did not release it.
        // We decide whether to retry by checking lock_may_be_available()
        // Since this will break the lock in case it is expired.
        $retry = $retry ? FALSE : lock_may_be_available($name);
      }
      // We only retry in case the first attempt failed, but we then broke
      // an expired lock.
    } while ($retry);
  }
  return isset($locks[$name]);
}
```

---
_Drupal 7.103 · [includes/lock.inc](https://github.com/drupal/drupal/blob/7.103/includes/lock.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
