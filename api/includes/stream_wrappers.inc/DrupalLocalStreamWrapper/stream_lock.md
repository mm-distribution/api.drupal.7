# DrupalLocalStreamWrapper::stream_lock()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 439–445 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L439-L445)
- **Class:** [DrupalLocalStreamWrapper](../DrupalLocalStreamWrapper.md)

## Signature

```php
public function stream_lock($operation)
```

## Documentation

```text
Support for flock().

@param $operation
  One of the following:
  - LOCK_SH to acquire a shared lock (reader).
  - LOCK_EX to acquire an exclusive lock (writer).
  - LOCK_UN to release a lock (shared or exclusive).
  - LOCK_NB if you don't want flock() to block while locking (not
    supported on Windows).

@return
  Always returns TRUE at the present time.

@see http://php.net/manual/streamwrapper.stream-lock.php
```

## Code

```php
  public function stream_lock($operation) {
    if (in_array($operation, array(LOCK_SH, LOCK_EX, LOCK_UN, LOCK_NB))) {
      return flock($this->handle, $operation);
    }

    return TRUE;
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
