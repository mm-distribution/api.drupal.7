# lock_wait()

- **Type:** Function
- **File:** [`includes/lock.inc`](_file.md), lines 222–256 · [local source](../../../source/includes/lock.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/lock.inc#L222-L256)
- **Topics:** [lock](../../topics/lock.md)

## Signature

```php
function lock_wait($name, $delay = 30)
```

## Documentation

```text
Wait for a lock to be available.

This function may be called in a request that fails to acquire a desired
lock. This will block further execution until the lock is available or the
specified delay in seconds is reached. This should not be used with locks
that are acquired very frequently, since the lock is likely to be acquired
again by a different request while waiting.

@param $name
  The name of the lock.
@param $delay
  The maximum number of seconds to wait, as an integer.

@return
  TRUE if the lock holds, FALSE if it is available.
```

## Code

```php
function lock_wait($name, $delay = 30) {
  // Pause the process for short periods between calling
  // lock_may_be_available(). This prevents hitting the database with constant
  // database queries while waiting, which could lead to performance issues.
  // However, if the wait period is too long, there is the potential for a
  // large number of processes to be blocked waiting for a lock, especially
  // if the item being rebuilt is commonly requested. To address both of these
  // concerns, begin waiting for 25ms, then add 25ms to the wait period each
  // time until it reaches 500ms. After this point polling will continue every
  // 500ms until $delay is reached.

  // $delay is passed in seconds, but we will be using usleep(), which takes
  // microseconds as a parameter. Multiply it by 1 million so that all
  // further numbers are equivalent.
  $delay = (int) $delay * 1000000;

  // Begin sleeping at 25ms.
  $sleep = 25000;
  while ($delay > 0) {
    // This function should only be called by a request that failed to get a
    // lock, so we sleep first to give the parallel request a chance to finish
    // and release the lock.
    usleep($sleep);
    // After each sleep, increase the value of $sleep until it reaches
    // 500ms, to reduce the potential for a lock stampede.
    $delay = $delay - $sleep;
    $sleep = min(500000, $sleep + 25000, $delay);
    if (lock_may_be_available($name)) {
      // No longer need to wait.
      return FALSE;
    }
  }
  // The caller must still wait longer to get the lock.
  return TRUE;
}
```

---
_Drupal 7.103 · [includes/lock.inc](https://github.com/drupal/drupal/blob/7.103/includes/lock.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
