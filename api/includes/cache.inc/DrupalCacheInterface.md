# DrupalCacheInterface

- **Type:** Interface
- **File:** [`includes/cache.inc`](_file.md), lines 229–314 · [local source](../../../source/includes/cache.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc#L229-L314)

## Signature

```php
interface DrupalCacheInterface
```

## Documentation

```text
Defines an interface for cache implementations.

All cache implementations have to implement this interface.
DrupalDatabaseCache provides the default implementation, which can be
consulted as an example.

To make Drupal use your implementation for a certain cache bin, you have to
set a variable with the name of the cache bin as its key and the name of
your class as its value. For example, if your implementation of
DrupalCacheInterface was called MyCustomCache, the following line would make
Drupal use it for the 'cache_page' bin:
@code
 variable_set('cache_class_cache_page', 'MyCustomCache');
@endcode

Additionally, you can register your cache implementation to be used by
default for all cache bins by setting the variable 'cache_default_class' to
the name of your implementation of the DrupalCacheInterface, e.g.
@code
 variable_set('cache_default_class', 'MyCustomCache');
@endcode

To implement a completely custom cache bin, use the same variable format:
@code
 variable_set('cache_class_custom_bin', 'MyCustomCache');
@endcode
To access your custom cache bin, specify the name of the bin when storing
or retrieving cached data:
@code
 cache_set($cid, $data, 'custom_bin', $expire);
 cache_get($cid, 'custom_bin');
@endcode

@see _cache_get_object()
@see DrupalDatabaseCache
```

## Methods (derived index)

- [get()](DrupalCacheInterface/get.md) — Returns data from the persistent cache.
- [getMultiple()](DrupalCacheInterface/getMultiple.md) — Returns data from the persistent cache when given an array of cache IDs.
- [set()](DrupalCacheInterface/set.md) — Stores data in the persistent cache.
- [clear()](DrupalCacheInterface/clear.md) — Expires data from the cache.
- [isEmpty()](DrupalCacheInterface/isEmpty.md) — Checks if a cache bin is empty.

---
_Drupal 7.103 · [includes/cache.inc](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
