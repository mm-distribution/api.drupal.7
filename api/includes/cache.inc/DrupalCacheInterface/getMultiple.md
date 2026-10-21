# DrupalCacheInterface::getMultiple()

- **Type:** Method
- **File:** [`includes/cache.inc`](../_file.md), lines 256–256 · [local source](../../../../source/includes/cache.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc#L256)
- **Class:** [DrupalCacheInterface](../DrupalCacheInterface.md)

## Signature

```php
function getMultiple(&$cids);
```

## Documentation

```text
Returns data from the persistent cache when given an array of cache IDs.

@param $cids
  An array of cache IDs for the data to retrieve. This is passed by
  reference, and will have the IDs successfully returned from cache
  removed.

@return
  An array of the items successfully returned from cache indexed by cid.
```

## Code

```php
   function getMultiple(&$cids);
```

---
_Drupal 7.103 · [includes/cache.inc](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
