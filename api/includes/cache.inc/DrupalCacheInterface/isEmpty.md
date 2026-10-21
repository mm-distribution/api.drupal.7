# DrupalCacheInterface::isEmpty()

- **Type:** Method
- **File:** [`includes/cache.inc`](../_file.md), lines 313–313 · [local source](../../../../source/includes/cache.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc#L313)
- **Class:** [DrupalCacheInterface](../DrupalCacheInterface.md)

## Signature

```php
function isEmpty();
```

## Documentation

```text
Checks if a cache bin is empty.

A cache bin is considered empty if it does not contain any valid data for
any cache ID.

@return
  TRUE if the cache bin specified is empty.
```

## Code

```php
  function isEmpty();
```

---
_Drupal 7.103 · [includes/cache.inc](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
