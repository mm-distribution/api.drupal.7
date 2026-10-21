# system_cron()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 3079–3142 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L3079-L3142)
- **Module/theme:** system
- **Implements:** [hook_cron()](../system.api.php/hook_cron.md)

## Signature

```php
function system_cron()
```

## Documentation

```text
Implements hook_cron().

Remove older rows from flood and batch table. Remove old temporary files.
```

## Code

```php
function system_cron() {
  // Cleanup the flood.
  db_delete('flood')
    ->condition('expiration', REQUEST_TIME, '<')
    ->execute();

  // Remove temporary files that are older than DRUPAL_MAXIMUM_TEMP_FILE_AGE.
  // Use separate placeholders for the status to avoid a bug in some versions
  // of PHP. See http://drupal.org/node/352956.
  $result = db_query('SELECT fid FROM {file_managed} WHERE status <> :permanent AND timestamp < :timestamp', array(
    ':permanent' => FILE_STATUS_PERMANENT,
    ':timestamp' => REQUEST_TIME - DRUPAL_MAXIMUM_TEMP_FILE_AGE
  ));
  foreach ($result as $row) {
    if ($file = file_load($row->fid)) {
      $references = file_usage_list($file);
      if (empty($references)) {
        if (!file_delete($file)) {
          watchdog('file system', 'Could not delete temporary file "%path" during garbage collection', array('%path' => $file->uri), WATCHDOG_ERROR);
        }
      }
      else {
        watchdog('file system', 'Did not delete temporary file "%path" during garbage collection, because it is in use by the following modules: %modules.', array('%path' => $file->uri, '%modules' => implode(', ', array_keys($references))), WATCHDOG_INFO);
      }
    }
  }

  // Delete expired cache entries.
  // Avoid invoking hook_flush_cashes() on every cron run because some modules
  // use this hook to perform expensive rebuilding operations (which are only
  // designed to happen on full cache clears), rather than just returning a
  // list of cache tables to be cleared.
  $cache_object = cache_get('system_cache_tables');
  if (empty($cache_object)) {
    $core = array('cache', 'cache_path', 'cache_filter', 'cache_page', 'cache_form', 'cache_menu');
    $cache_tables = array_merge(module_invoke_all('flush_caches'), $core);
    cache_set('system_cache_tables', $cache_tables);
  }
  else {
    $cache_tables = $cache_object->data;
  }
  foreach ($cache_tables as $table) {
    cache_clear_all(NULL, $table);
  }

  // Cleanup the batch table and the queue for failed batches.
  db_delete('batch')
    ->condition('timestamp', REQUEST_TIME - 864000, '<')
    ->execute();
  db_delete('queue')
    ->condition('created', REQUEST_TIME - 864000, '<')
    ->condition('name', 'drupal_batch:%', 'LIKE')
    ->execute();

  // Reset expired items in the default queue implementation table. If that's
  // not used, this will simply be a no-op.
  db_update('queue')
    ->fields(array(
      'expire' => 0,
    ))
    ->condition('expire', 0, '<>')
    ->condition('expire', REQUEST_TIME, '<')
    ->execute();
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
