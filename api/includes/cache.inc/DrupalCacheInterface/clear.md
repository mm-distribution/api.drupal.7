# DrupalCacheInterface::clear()

- **Type:** Method
- **File:** [`includes/cache.inc`](../_file.md), lines 302–302 · [local source](../../../../source/includes/cache.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc#L302)
- **Class:** [DrupalCacheInterface](../DrupalCacheInterface.md)

## Signature

```php
function clear($cid = NULL, $wildcard = FALSE);
```

## Documentation

```text
Expires data from the cache.

If called without arguments, expirable entries will be cleared from the
cache_page and cache_block bins.

@param $cid
  If set, the cache ID or an array of cache IDs. Otherwise, all cache
  entries that can expire are deleted. The $wildcard argument will be
  ignored if set to NULL.
@param $wildcard
  If TRUE, the $cid argument must contain a string value and cache IDs
  starting with $cid are deleted in addition to the exact cache ID
  specified by $cid. If $wildcard is TRUE and $cid is '*', the entire
  cache is emptied.
```

## Code

```php
  function clear($cid = NULL, $wildcard = FALSE);
```

---
_Drupal 7.103 · [includes/cache.inc](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
