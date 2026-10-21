# DrupalDatabaseCache::get()

- **Type:** Method
- **File:** [`includes/cache.inc`](../_file.md), lines 338–342 · [local source](../../../../source/includes/cache.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc#L338-L342)
- **Class:** [DrupalDatabaseCache](../DrupalDatabaseCache.md)

## Signature

```php
function get($cid)
```

## Documentation

```text
Implements DrupalCacheInterface::get().
```

## Code

```php
  function get($cid) {
    $cids = array($cid);
    $cache = $this->getMultiple($cids);
    return reset($cache);
  }
```

---
_Drupal 7.103 · [includes/cache.inc](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
