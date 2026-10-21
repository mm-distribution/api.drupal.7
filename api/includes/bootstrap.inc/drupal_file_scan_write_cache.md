# drupal_file_scan_write_cache()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 1220–1229 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L1220-L1229)

## Signature

```php
function drupal_file_scan_write_cache()
```

## Documentation

```text
Writes the file scan cache to the persistent cache.

This cache stores all files marked as missing or moved after a file scan
to prevent unnecessary file scans in subsequent requests. This cache is
cleared in system_list_reset() (i.e. after a module/theme rebuild).
```

## Code

```php
function drupal_file_scan_write_cache() {
  // Only write to the persistent cache if requested, and if we know that any
  // data previously in the cache was successfully loaded and merged in by
  // _drupal_file_scan_cache().
  $file_scans = &_drupal_file_scan_cache();
  if (isset($file_scans['#write_cache']) && isset($file_scans['#cache_merge_done'])) {
    unset($file_scans['#write_cache']);
    cache_set('_drupal_file_scan_cache', $file_scans, 'cache_bootstrap');
  }
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
