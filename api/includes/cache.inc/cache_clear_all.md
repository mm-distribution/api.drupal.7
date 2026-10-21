# cache_clear_all()

- **Type:** Function
- **File:** [`includes/cache.inc`](_file.md), lines 163–174 · [local source](../../../source/includes/cache.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc#L163-L174)

## Signature

```php
function cache_clear_all($cid = NULL, $bin = NULL, $wildcard = FALSE)
```

## Documentation

```text
Expires data from the cache.

If called with the arguments $cid and $bin set to NULL or omitted, then
expirable entries will be cleared from the cache_page and cache_block bins,
and the $wildcard argument is ignored.

@param $cid
  If set, the cache ID or an array of cache IDs. Otherwise, all cache entries
  that can expire are deleted. The $wildcard argument will be ignored if set
  to NULL.
@param $bin
  If set, the cache bin to delete from. Mandatory argument if $cid is set.
@param $wildcard
  If TRUE, the $cid argument must contain a string value and cache IDs
  starting with $cid are deleted in addition to the exact cache ID specified
  by $cid. If $wildcard is TRUE and $cid is '*', the entire cache is emptied.
```

## Code

```php
function cache_clear_all($cid = NULL, $bin = NULL, $wildcard = FALSE) {
  if (!isset($cid) && !isset($bin)) {
    // Clear the block cache first, so stale data will
    // not end up in the page cache.
    if (module_exists('block')) {
      cache_clear_all(NULL, 'cache_block');
    }
    cache_clear_all(NULL, 'cache_page');
    return;
  }
  return _cache_get_object($bin)->clear($cid, $wildcard);
}
```

---
_Drupal 7.103 · [includes/cache.inc](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
