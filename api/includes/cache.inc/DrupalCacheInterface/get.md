# DrupalCacheInterface::get()

- **Type:** Method
- **File:** [`includes/cache.inc`](../_file.md), lines 243–243 · [local source](../../../../source/includes/cache.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc#L243)
- **Class:** [DrupalCacheInterface](../DrupalCacheInterface.md)

## Signature

```php
function get($cid);
```

## Documentation

```text
Returns data from the persistent cache.

Data may be stored as either plain text or as serialized data. cache_get()
will automatically return unserialized objects and arrays.

@param $cid
  The cache ID of the data to retrieve.

@return
  The cache or FALSE on failure.
```

## Code

```php
  function get($cid);
```

---
_Drupal 7.103 · [includes/cache.inc](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
