# DrupalCacheArray::set()

- **Type:** Method
- **File:** [`includes/bootstrap.inc`](../_file.md), lines 438–451 · [local source](../../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L438-L451)
- **Class:** [DrupalCacheArray](../DrupalCacheArray.md)

## Signature

```php
protected function set($data, $lock = TRUE)
```

## Documentation

```text
Writes a value to the persistent cache immediately.

@param $data
  The data to write to the persistent cache.
@param $lock
  Whether to acquire a lock before writing to cache.
```

## Code

```php
  protected function set($data, $lock = TRUE) {
    // Lock cache writes to help avoid stampedes.
    // To implement locking for cache misses, override __construct().
    $lock_name = $this->cid . ':' . $this->bin;
    if (!$lock || lock_acquire($lock_name)) {
      if ($cached = cache_get($this->cid, $this->bin)) {
        $data = $cached->data + $data;
      }
      cache_set($this->cid, $data, $this->bin);
      if ($lock) {
        lock_release($lock_name);
      }
    }
  }
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
