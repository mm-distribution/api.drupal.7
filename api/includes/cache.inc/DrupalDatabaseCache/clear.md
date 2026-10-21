# DrupalDatabaseCache::clear()

- **Type:** Method
- **File:** [`includes/cache.inc`](../_file.md), lines 487–555 · [local source](../../../../source/includes/cache.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc#L487-L555)
- **Class:** [DrupalDatabaseCache](../DrupalDatabaseCache.md)

## Signature

```php
function clear($cid = NULL, $wildcard = FALSE)
```

## Documentation

```text
Implements DrupalCacheInterface::clear().
```

## Code

```php
  function clear($cid = NULL, $wildcard = FALSE) {
    global $user;

    if (empty($cid)) {
      if (variable_get('cache_lifetime', 0)) {
        // We store the time in the current user's session. We then simulate
        // that the cache was flushed for this user by not returning cached
        // data that was cached before the timestamp.
        $_SESSION['cache_expiration'][$this->bin] = REQUEST_TIME;

        $cache_flush = variable_get('cache_flush_' . $this->bin, 0);
        if ($cache_flush == 0) {
          // This is the first request to clear the cache, start a timer.
          variable_set('cache_flush_' . $this->bin, REQUEST_TIME);
        }
        elseif (REQUEST_TIME > ($cache_flush + variable_get('cache_lifetime', 0))) {
          // Clear the cache for everyone, cache_lifetime seconds have
          // passed since the first request to clear the cache.
          db_delete($this->bin)
            ->condition('expire', CACHE_PERMANENT, '<>')
            ->condition('expire', REQUEST_TIME, '<')
            ->execute();
          variable_set('cache_flush_' . $this->bin, 0);
        }
      }
      else {
        // No minimum cache lifetime, flush all temporary cache entries now.
        db_delete($this->bin)
          ->condition('expire', CACHE_PERMANENT, '<>')
          ->condition('expire', REQUEST_TIME, '<')
          ->execute();
      }
    }
    else {
      if ($wildcard) {
        if ($cid == '*') {
          // Check if $this->bin is a cache table before truncating. Other
          // cache_clear_all() operations throw a PDO error in this situation,
          // so we don't need to verify them first. This ensures that non-cache
          // tables cannot be truncated accidentally.
          if ($this->isValidBin()) {
            db_truncate($this->bin)->execute();
          }
          else {
            throw new Exception(t('Invalid or missing cache bin specified: %bin', array('%bin' => $this->bin)));
          }
        }
        else {
          db_delete($this->bin)
            ->condition('cid', db_like($cid) . '%', 'LIKE')
            ->execute();
        }
      }
      elseif (is_array($cid)) {
        // Delete in chunks when a large array is passed.
        do {
          db_delete($this->bin)
            ->condition('cid', array_splice($cid, 0, 1000), 'IN')
            ->execute();
        }
        while (count($cid));
      }
      else {
        db_delete($this->bin)
          ->condition('cid', $cid)
          ->execute();
      }
    }
  }
```

---
_Drupal 7.103 · [includes/cache.inc](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
