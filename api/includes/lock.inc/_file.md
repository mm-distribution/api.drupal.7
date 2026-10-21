# includes/lock.inc

- **Source:** [local](../../../source/includes/lock.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/lock.inc) · 294 lines

## File documentation

```text
@file
A database-mediated implementation of a locking mechanism.
```

## Functions (derived index)

- [lock_initialize()](lock_initialize.md) — Initialize the locking system.
- [_lock_id()](_lock_id.md) — Helper function to get this request's unique id.
- [lock_acquire()](lock_acquire.md) — Acquire (or renew) a lock, but do not block if it fails.
- [lock_may_be_available()](lock_may_be_available.md) — Check if lock acquired by a different process may be available.
- [lock_wait()](lock_wait.md) — Wait for a lock to be available.
- [lock_release()](lock_release.md) — Release a lock previously acquired by lock_acquire().
- [lock_release_all()](lock_release_all.md) — Release all previously acquired locks.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
