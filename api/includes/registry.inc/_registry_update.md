# _registry_update()

- **Type:** Function
- **File:** [`includes/registry.inc`](_file.md), lines 21–135 · [local source](../../../source/includes/registry.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/registry.inc#L21-L135)
- **Topics:** [registry](../../topics/registry.md)

## Signature

```php
function _registry_update()
```

## Documentation

```text
Does the work for registry_update().
```

## Code

```php
function _registry_update() {
  // The registry serves as a central autoloader for all classes, including
  // the database query builders. However, the registry rebuild process
  // requires write ability to the database, which means having access to the
  // query builders that require the registry in order to be loaded. That
  // causes a fatal race condition. Therefore we manually include the
  // appropriate query builders for the currently active database before the
  // registry rebuild process runs.
  $connection_info = Database::getConnectionInfo();
  $driver = $connection_info['default']['driver'];
  require_once DRUPAL_ROOT . '/includes/database/query.inc';
  require_once DRUPAL_ROOT . '/includes/database/select.inc';
  require_once DRUPAL_ROOT . '/includes/database/' . $driver . '/query.inc';

  // During the first registry rebuild in a request, we check all the files.
  // During subsequent rebuilds, we only add new files. It makes the rebuilding
  // process faster during installation of modules.
  static $check_existing_files = TRUE;

  // Get current list of modules and their files.
  $modules = db_query("SELECT * FROM {system} WHERE type = 'module'")->fetchAll();
  // Get the list of files we are going to parse.
  $files = array();
  foreach ($modules as &$module) {
    $module->info = unserialize($module->info);
    $dir = dirname($module->filename);

    // Store the module directory for use in hook_registry_files_alter().
    $module->dir = $dir;

    if ($module->status) {
      // Add files for enabled modules to the registry.
      foreach ($module->info['files'] as $file) {
        $files["$dir/$file"] = array('module' => $module->name, 'weight' => $module->weight);
      }
    }
  }
  foreach (file_scan_directory('includes', '/\.inc$/') as $filename => $file) {
    $files["$filename"] = array('module' => '', 'weight' => 0);
  }

  // Initialize an empty array for the unchanged files.
  $unchanged_files = array();

  $transaction = db_transaction();
  try {
    // Allow modules to manually modify the list of files before the registry
    // parses them. The $modules array provides the .info file information, which
    // includes the list of files registered to each module. Any files in the
    // list can then be added to the list of files that the registry will parse,
    // or modify attributes of a file.
    drupal_alter('registry_files', $files, $modules);

    foreach (registry_get_parsed_files() as $filename => $file) {
      // Add the hash for those files we have already parsed.
      if (isset($files[$filename])) {
        if ($check_existing_files === TRUE) {
          $files[$filename]['hash'] = $file['hash'];
        }
        else {
          // Ignore that file for this request, it has been parsed previously
          // and it is unlikely it has changed.
          unset($files[$filename]);
          $unchanged_files[$filename] = $file;
        }
      }
      else {
        // Flush the registry of resources in files that are no longer on disc
        // or are in files that no installed modules require to be parsed.
        db_delete('registry')
          ->condition('filename', $filename)
          ->execute();
        db_delete('registry_file')
          ->condition('filename', $filename)
          ->execute();
      }
    }

    $parsed_files = _registry_parse_files($files);

    // Add unchanged files to the files.
    $files += $unchanged_files;

    $unchanged_resources = array();
    $lookup_cache = array();
    if ($cache = cache_get('lookup_cache', 'cache_bootstrap')) {
      $lookup_cache = $cache->data;
    }
    foreach ($lookup_cache as $key => $file) {
      // If the file for this cached resource is carried over unchanged from
      // the last registry build, then we can safely re-cache it.
      if ($file && isset($files[$file]) && !in_array($file, $parsed_files, TRUE)) {
        $unchanged_resources[$key] = $file;
      }
    }
  }
  catch (Exception $e) {
    $transaction->rollback();
    watchdog_exception('registry', $e);
    throw $e;
  }

  module_implements('', FALSE, TRUE);
  _registry_check_code(REGISTRY_RESET_LOOKUP_CACHE);

  // During the next run in this request, don't bother re-checking existing
  // files.
  $check_existing_files = FALSE;

  // We have some unchanged resources, warm up the cache - no need to pay
  // for looking them up again.
  if (count($unchanged_resources) > 0) {
    cache_set('lookup_cache', $unchanged_resources, 'cache_bootstrap');
  }
}
```

---
_Drupal 7.103 · [includes/registry.inc](https://github.com/drupal/drupal/blob/7.103/includes/registry.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
