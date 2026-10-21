# cache_is_empty()

- **Type:** Function
- **File:** [`includes/cache.inc`](_file.md), lines 188–190 · [local source](../../../source/includes/cache.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc#L188-L190)

## Signature

```php
function cache_is_empty($bin)
```

## Documentation

```text
Checks if a cache bin is empty.

A cache bin is considered empty if it does not contain any valid data for any
cache ID.

@param $bin
  The cache bin to check.

@return
  TRUE if the cache bin specified is empty.
```

## Code

```php
function cache_is_empty($bin) {
  return _cache_get_object($bin)->isEmpty();
}
```

---
_Drupal 7.103 · [includes/cache.inc](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
