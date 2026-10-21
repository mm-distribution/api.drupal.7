# Locking mechanisms

- **Topic id:** `lock`
- **Defined in:** [`includes/lock.inc`](../includes/lock.inc/_file.md), line 8 · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/lock.inc#L8)

## Documentation

```text
@defgroup lock Locking mechanisms
@{
Functions to coordinate long-running operations across requests.

In most environments, multiple Drupal page requests (a.k.a. threads or
processes) will execute in parallel. This leads to potential conflicts or
race conditions when two requests execute the same code at the same time. A
common example of this is a rebuild like menu_rebuild() where we invoke many
hook implementations to get and process data from all active modules, and
then delete the current data in the database to insert the new afterwards.

To avoid these types of conflicts, Drupal has a cooperative, advisory lock
system. Any long-running operation that could potentially be attempted in
parallel by multiple requests should try to acquire a lock before
proceeding. By obtaining a lock, one request notifies any other requests that
a specific operation is in progress which must not be executed in parallel.

To use this API, pick a unique name for the lock. A sensible choice is the
name of the function performing the operation. Here is a simple example:
@code
function mymodule_long_operation() {
  if (lock_acquire('mymodule_long_operation')) {
    // Do the long operation here.
    // ...
    lock_release('mymodule_long_operation');
  }
}
@endcode

If a function acquires a lock it should always release it when the
operation is complete by calling lock_release(), as in the example.

A function that has acquired a lock may attempt to renew a lock (extend the
duration of the lock) by calling lock_acquire() again during the operation.
Failure to renew a lock is indicative that another request has acquired
the lock, and that the current operation may need to be aborted.

If a function fails to acquire a lock it may either immediately return, or
it may call lock_wait() if the rest of the current page request requires
that the operation in question be complete. After lock_wait() returns,
the function may again attempt to acquire the lock, or may simply allow the
page request to proceed on the assumption that a parallel request completed
the operation.

lock_acquire() and lock_wait() will automatically break (delete) a lock
whose duration has exceeded the timeout specified when it was acquired.

The following limitations in this implementation should be carefully noted:
- Time: Timestamps are derived from the local system clock of the environment
  the code is executing in. The orderly progression of time from this
  viewpoint can be disrupted by external events such as NTP synchronization
  and operator intervention. Where multiple web servers are involved in
  serving the site, they will have their own independent clocks, introducing
  another source of error in the time keeping process. Timeout values applied
  to locks must therefore be considered approximate, and should not be relied
  upon.
- Uniqueness: Uniqueness of lock names is not enforced. The impact of the
  use of a common lock name will depend on what processes and resources the
  lock is being used to manage.
- Sharing: There is limited support for resources shared across sites.
  The locks are stored as rows in the semaphore table and, as such, they
  have the same visibility as the table. If resources managed by a lock are
  shared across sites then the semaphore table must be shared across sites
  as well. This is a binary situation: either all resources are shared and
  the semaphore table is shared or no resources are shared and the semaphore
  table is not shared. Mixed mode operation is not supported.

Alternative implementations of this API (such as APC) may be substituted
by setting the 'lock_inc' variable to an alternate include filepath. Since
this is an API intended to support alternative implementations, code using
this API should never rely upon specific implementation details (for example
no code should look for or directly modify a lock in the {semaphore} table).
```

## Members (derived, 7)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [_lock_id()](../includes/lock.inc/_lock_id.md) (function) — Helper function to get this request's unique id.
- [lock_acquire()](../includes/lock.inc/lock_acquire.md) (function) — Acquire (or renew) a lock, but do not block if it fails.
- [lock_initialize()](../includes/lock.inc/lock_initialize.md) (function) — Initialize the locking system.
- [lock_may_be_available()](../includes/lock.inc/lock_may_be_available.md) (function) — Check if lock acquired by a different process may be available.
- [lock_release()](../includes/lock.inc/lock_release.md) (function) — Release a lock previously acquired by lock_acquire().
- [lock_release_all()](../includes/lock.inc/lock_release_all.md) (function) — Release all previously acquired locks.
- [lock_wait()](../includes/lock.inc/lock_wait.md) (function) — Wait for a lock to be available.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
