# lock_release_all()

- **Type:** Function
- **File:** [`includes/lock.inc`](_file.md), lines 279–289 · [local source](../../../source/includes/lock.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/lock.inc#L279-L289)
- **Topics:** [lock](../../topics/lock.md)

## Signature

```php
function lock_release_all($lock_id = NULL)
```

## Documentation

```text
Release all previously acquired locks.
```

## Code

```php
function lock_release_all($lock_id = NULL) {
  global $locks;

  $locks = array();
  if (empty($lock_id)) {
    $lock_id = _lock_id();
  }
  db_delete('semaphore')
    ->condition('value', $lock_id)
    ->execute();
}
```

---
_Drupal 7.103 · [includes/lock.inc](https://github.com/drupal/drupal/blob/7.103/includes/lock.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
