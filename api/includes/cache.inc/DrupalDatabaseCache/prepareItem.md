# DrupalDatabaseCache::prepareItem()

- **Type:** Method
- **File:** [`includes/cache.inc`](../_file.md), lines 432–453 · [local source](../../../../source/includes/cache.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc#L432-L453)
- **Class:** [DrupalDatabaseCache](../DrupalDatabaseCache.md)

## Signature

```php
protected function prepareItem($cache)
```

## Documentation

```text
Prepares a cached item.

Checks that items are either permanent or did not expire, and unserializes
data as appropriate.

@param $cache
  An item loaded from cache_get() or cache_get_multiple().

@return
  The item with data unserialized as appropriate or FALSE if there is no
  valid item to load.
```

## Code

```php
  protected function prepareItem($cache) {
    global $user;

    if (!isset($cache->data)) {
      return FALSE;
    }
    // If the cached data is temporary and subject to a per-user minimum
    // lifetime, compare the cache entry timestamp with the user session
    // cache_expiration timestamp. If the cache entry is too old, ignore it.
    if ($cache->expire != CACHE_PERMANENT && variable_get('cache_lifetime', 0) && isset($_SESSION['cache_expiration'][$this->bin]) && $_SESSION['cache_expiration'][$this->bin] > $cache->created) {
      // Ignore cache data that is too old and thus not valid for this user.
      return FALSE;
    }

    // If the data is permanent or not subject to a minimum cache lifetime,
    // unserialize and return the cached data.
    if ($cache->serialized) {
      $cache->data = unserialize($cache->data);
    }

    return $cache;
  }
```

---
_Drupal 7.103 · [includes/cache.inc](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
