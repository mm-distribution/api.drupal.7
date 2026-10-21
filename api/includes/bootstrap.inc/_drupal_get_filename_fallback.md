# _drupal_get_filename_fallback()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 981–1019 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L981-L1019)

## Signature

```php
function _drupal_get_filename_fallback($type, $name, $trigger_error, $database_unavailable)
```

## Documentation

```text
Performs a cached file system scan as a fallback when searching for a file.

This function looks for the requested file by triggering a file scan,
caching the new location if the file has moved and caching the miss
if the file is missing. If a file had been marked as missing in a previous
file scan, or if it has been marked as moved and is still in the last known
location, no new file scan will be performed.

@param string $type
  The type of the item (theme, theme_engine, module, profile).
@param string $name
  The name of the item for which the filename is requested.
@param bool $trigger_error
  Whether to trigger an error when a file is missing or has unexpectedly
  moved.
@param bool $database_unavailable
  Whether this function is being called because the Drupal database could
  not be queried for the file's location.

@return
  The filename of the requested item or NULL if the item is not found.

@see drupal_get_filename()
```

## Code

```php
function _drupal_get_filename_fallback($type, $name, $trigger_error, $database_unavailable) {
  $file_scans = &_drupal_file_scan_cache();
  $filename = NULL;

  // If the cache indicates that the item is missing, or we can verify that the
  // item exists in the location the cache says it exists in, use that.
  if (isset($file_scans[$type][$name]) && ($file_scans[$type][$name] === FALSE || file_exists($file_scans[$type][$name]))) {
    $filename = $file_scans[$type][$name];
  }
  // Otherwise, perform a new file scan to find the item.
  else {
    $filename = _drupal_get_filename_perform_file_scan($type, $name);
    // Update the static cache, and mark the persistent cache for updating at
    // the end of the page request. See drupal_file_scan_write_cache().
    $file_scans[$type][$name] = $filename;
    $file_scans['#write_cache'] = TRUE;
  }

  // If requested, trigger a user-level warning about the missing or
  // unexpectedly moved file. If the database was unavailable, do not trigger a
  // warning in the latter case, though, since if the {system} table could not
  // be queried there is no way to know if the location found here was
  // "unexpected" or not.
  if ($trigger_error) {
    $error_type = $filename === FALSE ? 'missing' : 'moved';
    if ($error_type == 'missing' || !$database_unavailable) {
      _drupal_get_filename_fallback_trigger_error($type, $name, $error_type);
    }
  }

  // The cache stores FALSE for files that aren't found (to be able to
  // distinguish them from files that have not yet been searched for), but
  // drupal_get_filename() expects NULL for these instead, so convert to NULL
  // before returning.
  if ($filename === FALSE) {
    $filename = NULL;
  }
  return $filename;
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
