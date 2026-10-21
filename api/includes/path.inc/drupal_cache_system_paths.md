# drupal_cache_system_paths()

- **Type:** Function
- **File:** [`includes/path.inc`](_file.md), lines 203–218 · [local source](../../../source/includes/path.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/path.inc#L203-L218)

## Signature

```php
function drupal_cache_system_paths()
```

## Documentation

```text
Cache system paths for a page.

Cache an array of the system paths available on each page. We assume
that aliases will be needed for the majority of these paths during
subsequent requests, and load them in a single query during
drupal_lookup_path().
```

## Code

```php
function drupal_cache_system_paths() {
  // Check if the system paths for this page were loaded from cache in this
  // request to avoid writing to cache on every request.
  $cache = &drupal_static('drupal_lookup_path', array());
  if (empty($cache['system_paths']) && !empty($cache['map'])) {
    // Generate a cache ID (cid) specifically for this page.
    $cid = current_path();
    // The static $map array used by drupal_lookup_path() includes all
    // system paths for the page request.
    if ($paths = current($cache['map'])) {
      $data = array_keys($paths);
      $expire = REQUEST_TIME + (60 * 60 * 24);
      cache_set($cid, $data, 'cache_path', $expire);
    }
  }
}
```

---
_Drupal 7.103 · [includes/path.inc](https://github.com/drupal/drupal/blob/7.103/includes/path.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
