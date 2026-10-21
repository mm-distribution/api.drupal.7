# _cache_get_object()

- **Type:** Function
- **File:** [`includes/cache.inc`](_file.md), lines 23–35 · [local source](../../../source/includes/cache.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc#L23-L35)

## Signature

```php
function _cache_get_object($bin)
```

## Documentation

```text
Gets the cache object for a cache bin.

By default, this returns an instance of the DrupalDatabaseCache class.
Classes implementing DrupalCacheInterface can register themselves both as a
default implementation and for specific bins.

@param $bin
  The cache bin for which the cache object should be returned.

@return DrupalCacheInterface
  The cache object associated with the specified bin.

@see DrupalCacheInterface
```

## Code

```php
function _cache_get_object($bin) {
  // We do not use drupal_static() here because we do not want to change the
  // storage of a cache bin mid-request.
  static $cache_objects;
  if (!isset($cache_objects[$bin])) {
    $class = variable_get('cache_class_' . $bin);
    if (!isset($class)) {
      $class = variable_get('cache_default_class', 'DrupalDatabaseCache');
    }
    $cache_objects[$bin] = new $class($bin);
  }
  return $cache_objects[$bin];
}
```

---
_Drupal 7.103 · [includes/cache.inc](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
