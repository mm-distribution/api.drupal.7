# drupal_get_complete_schema()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 3415–3464 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L3415-L3464)
- **Topics:** [schemaapi](../../topics/schemaapi.md)

## Signature

```php
function drupal_get_complete_schema($rebuild = FALSE)
```

## Documentation

```text
Gets the whole database schema.

The returned schema will include any modifications made by any
module that implements hook_schema_alter().

@param $rebuild
  If true, the schema will be rebuilt instead of retrieved from the cache.
```

## Code

```php
function drupal_get_complete_schema($rebuild = FALSE) {
  static $schema = array();

  if (empty($schema) || $rebuild) {
    // Try to load the schema from cache.
    if (!$rebuild && $cached = cache_get('schema')) {
      $schema = $cached->data;
    }
    // Otherwise, rebuild the schema cache.
    else {
      $schema = array();
      // Load the .install files to get hook_schema.
      // On some databases this function may be called before bootstrap has
      // been completed, so we force the functions we need to load just in case.
      if (function_exists('module_load_all_includes')) {
        // This function can be called very early in the bootstrap process, so
        // we force the module_list() cache to be refreshed to ensure that it
        // contains the complete list of modules before we go on to call
        // module_load_all_includes().
        module_list(TRUE);
        module_load_all_includes('install');
      }

      require_once DRUPAL_ROOT . '/includes/common.inc';
      // Invoke hook_schema for all modules.
      foreach (module_implements('schema') as $module) {
        // Cast the result of hook_schema() to an array, as a NULL return value
        // would cause array_merge() to set the $schema variable to NULL as well.
        // That would break modules which use $schema further down the line.
        $current = (array) module_invoke($module, 'schema');
        // Set 'module' and 'name' keys for each table, and remove descriptions,
        // as they needlessly slow down cache_get() for every single request.
        _drupal_schema_initialize($current, $module);
        $schema = array_merge($schema, $current);
      }

      drupal_alter('schema', $schema);
      // If the schema is empty, avoid saving it: some database engines require
      // the schema to perform queries, and this could lead to infinite loops.
      if (!empty($schema) && (drupal_get_bootstrap_phase() == DRUPAL_BOOTSTRAP_FULL)) {
        cache_set('schema', $schema);
      }
      if ($rebuild) {
        cache_clear_all('schema:', 'cache', TRUE);
      }
    }
  }

  return $schema;
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
