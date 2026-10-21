# DrupalDatabaseCache::garbageCollection()

- **Type:** Method
- **File:** [`includes/cache.inc`](../_file.md), lines 383–417 · [local source](../../../../source/includes/cache.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc#L383-L417)
- **Class:** [DrupalDatabaseCache](../DrupalDatabaseCache.md)

## Signature

```php
protected function garbageCollection()
```

## Documentation

```text
Garbage collection for get() and getMultiple().

@param $bin
  The bin being requested.
```

## Code

```php
  protected function garbageCollection() {
    $cache_lifetime = variable_get('cache_lifetime', 0);

    // Clean-up the per-user cache expiration session data, so that the session
    // handler can properly clean-up the session data for anonymous users.
    if (isset($_SESSION['cache_expiration'])) {
      $expire = REQUEST_TIME - $cache_lifetime;
      foreach ($_SESSION['cache_expiration'] as $bin => $timestamp) {
        if ($timestamp < $expire) {
          unset($_SESSION['cache_expiration'][$bin]);
        }
      }
      if (!$_SESSION['cache_expiration']) {
        unset($_SESSION['cache_expiration']);
      }
    }

    // Garbage collection of temporary items is only necessary when enforcing
    // a minimum cache lifetime.
    if (!$cache_lifetime) {
      return;
    }
    // When cache lifetime is in force, avoid running garbage collection too
    // often since this will remove temporary cache items indiscriminately.
    $cache_flush = variable_get('cache_flush_' . $this->bin, 0);
    if ($cache_flush && ($cache_flush + $cache_lifetime <= REQUEST_TIME)) {
      // Reset the variable immediately to prevent a meltdown in heavy load situations.
      variable_set('cache_flush_' . $this->bin, 0);
      // Time to flush old cache data
      db_delete($this->bin)
        ->condition('expire', CACHE_PERMANENT, '<>')
        ->condition('expire', $cache_flush, '<=')
        ->execute();
    }
  }
```

---
_Drupal 7.103 · [includes/cache.inc](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
