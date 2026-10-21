# _drupal_file_scan_cache()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 1031–1058 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L1031-L1058)

## Signature

```php
function &_drupal_file_scan_cache()
```

## Documentation

```text
Returns the current list of cached file system scan results.

@return
  An associative array tracking the most recent file scan results for all
  files that have had scans performed. The keys are the type and name of the
  item that was searched for, and the values can be either:
  - Boolean FALSE if the item was not found in the file system.
  - A string pointing to the location where the item was found.
```

## Code

```php
function &_drupal_file_scan_cache() {
  $file_scans = &drupal_static(__FUNCTION__, array());

  // The file scan results are stored in a persistent cache (in addition to the
  // static cache) but because this function can be called before the
  // persistent cache is available, we must merge any items that were found
  // earlier in the page request into the results from the persistent cache.
  if (!isset($file_scans['#cache_merge_done'])) {
    try {
      if (function_exists('cache_get')) {
        $cache = cache_get('_drupal_file_scan_cache', 'cache_bootstrap');
        if (!empty($cache->data)) {
          // File scan results from the current request should take precedence
          // over the results from the persistent cache, since they are newer.
          $file_scans = drupal_array_merge_deep($cache->data, $file_scans);
        }
        // Set a flag to indicate that the persistent cache does not need to be
        // merged again.
        $file_scans['#cache_merge_done'] = TRUE;
      }
    }
    catch (Exception $e) {
      // Hide the error.
    }
  }

  return $file_scans;
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
