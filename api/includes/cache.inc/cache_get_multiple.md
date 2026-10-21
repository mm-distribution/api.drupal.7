# cache_get_multiple()

- **Type:** Function
- **File:** [`includes/cache.inc`](_file.md), lines 72–74 · [local source](../../../source/includes/cache.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc#L72-L74)

## Signature

```php
function cache_get_multiple(array &$cids, $bin = 'cache')
```

## Documentation

```text
Returns data from the persistent cache when given an array of cache IDs.

@param $cids
  An array of cache IDs for the data to retrieve. This is passed by
  reference, and will have the IDs successfully returned from cache removed.
@param $bin
  The cache bin where the data is stored.

@return
  An array of the items successfully returned from cache indexed by cid.
```

## Code

```php
function cache_get_multiple(array &$cids, $bin = 'cache') {
  return _cache_get_object($bin)->getMultiple($cids);
}
```

---
_Drupal 7.103 · [includes/cache.inc](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
