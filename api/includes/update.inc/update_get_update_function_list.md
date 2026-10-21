# update_get_update_function_list()

- **Type:** Function
- **File:** [`includes/update.inc`](_file.md), lines 1285–1304 · [local source](../../../source/includes/update.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/update.inc#L1285-L1304)

## Signature

```php
function update_get_update_function_list($starting_updates)
```

## Documentation

```text
Returns an organized list of update functions for a set of modules.

@param $starting_updates
  An array whose keys contain the names of modules and whose values contain
  the number of the first requested update for that module.

@return
  An array containing all the update functions that should be run for each
  module, including the provided starting update and all subsequent updates
  that are available. The keys of the array contain the module names, and
  each value is an ordered array of update functions, keyed by the update
  number.

@see update_resolve_dependencies()
```

## Code

```php
function update_get_update_function_list($starting_updates) {
  // Go through each module and find all updates that we need (including the
  // first update that was requested and any updates that run after it).
  $update_functions = array();
  foreach ($starting_updates as $module => $version) {
    $update_functions[$module] = array();
    $updates = drupal_get_schema_versions($module);
    if ($updates !== FALSE) {
      $max_version = max($updates);
      if ($version <= $max_version) {
        foreach ($updates as $update) {
          if ($update >= $version) {
            $update_functions[$module][$update] = $module . '_update_' . $update;
          }
        }
      }
    }
  }
  return $update_functions;
}
```

---
_Drupal 7.103 · [includes/update.inc](https://github.com/drupal/drupal/blob/7.103/includes/update.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
