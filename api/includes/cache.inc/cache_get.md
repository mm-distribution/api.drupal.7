# cache_get()

- **Type:** Function
- **File:** [`includes/cache.inc`](_file.md), lines 56–58 · [local source](../../../source/includes/cache.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc#L56-L58)

## Signature

```php
function cache_get($cid, $bin = 'cache')
```

## Documentation

```text
Returns data from the persistent cache.

Data may be stored as either plain text or as serialized data. cache_get
will automatically return unserialized objects and arrays.

@param $cid
  The cache ID of the data to retrieve.
@param $bin
  The cache bin to store the data in. Valid core values are 'cache_block',
  'cache_bootstrap', 'cache_field', 'cache_filter', 'cache_form',
  'cache_menu', 'cache_page', 'cache_path', 'cache_update' or 'cache' for
  the default cache.

@return
  The cache or FALSE on failure.

@see cache_set()
```

## Code

```php
function cache_get($cid, $bin = 'cache') {
  return _cache_get_object($bin)->get($cid);
}
```

---
_Drupal 7.103 · [includes/cache.inc](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
