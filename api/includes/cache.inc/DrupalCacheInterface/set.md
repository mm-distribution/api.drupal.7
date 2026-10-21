# DrupalCacheInterface::set()

- **Type:** Method
- **File:** [`includes/cache.inc`](../_file.md), lines 283–283 · [local source](../../../../source/includes/cache.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc#L283)
- **Class:** [DrupalCacheInterface](../DrupalCacheInterface.md)

## Signature

```php
function set($cid, $data, $expire = CACHE_PERMANENT);
```

## Documentation

```text
Stores data in the persistent cache.

@param $cid
  The cache ID of the data to store.
@param $data
  The data to store in the cache. Complex data types will be automatically
  serialized before insertion. Strings will be stored as plain text and not
  serialized. Some storage engines only allow objects up to a maximum of
  1MB in size to be stored by default. When caching large arrays or
  similar, take care to ensure $data does not exceed this size.
@param $expire
  (optional) Controls the maximum lifetime of this cache entry. Note that
  caches might be subject to clearing at any time, so this setting does not
  guarantee a minimum lifetime. With this in mind, the cache should not be
  used for data that must be kept during a cache clear, like sessions.

  Use one of the following values:
  - CACHE_PERMANENT: Indicates that the item should never be removed unless
    explicitly told to using cache_clear_all() with a cache ID.
  - CACHE_TEMPORARY: Indicates that the item should be removed at the next
    general cache wipe.
  - A Unix timestamp: Indicates that the item should be kept at least until
    the given time, after which it behaves like CACHE_TEMPORARY.
```

## Code

```php
  function set($cid, $data, $expire = CACHE_PERMANENT);
```

---
_Drupal 7.103 · [includes/cache.inc](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
