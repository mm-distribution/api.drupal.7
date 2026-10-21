# lock_release()

- **Type:** Function
- **File:** [`includes/lock.inc`](_file.md), lines 266–274 · [local source](../../../source/includes/lock.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/lock.inc#L266-L274)
- **Topics:** [lock](../../topics/lock.md)

## Signature

```php
function lock_release($name)
```

## Documentation

```text
Release a lock previously acquired by lock_acquire().

This will release the named lock if it is still held by the current request.

@param $name
  The name of the lock.
```

## Code

```php
function lock_release($name) {
  global $locks;

  unset($locks[$name]);
  db_delete('semaphore')
    ->condition('name', $name)
    ->condition('value', _lock_id())
    ->execute();
}
```

---
_Drupal 7.103 · [includes/lock.inc](https://github.com/drupal/drupal/blob/7.103/includes/lock.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
