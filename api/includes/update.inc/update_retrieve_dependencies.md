# update_retrieve_dependencies()

- **Type:** Function
- **File:** [`includes/update.inc`](_file.md), lines 1438–1489 · [local source](../../../source/includes/update.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/update.inc#L1438-L1489)

## Signature

```php
function update_retrieve_dependencies()
```

## Documentation

```text
Invokes hook_update_dependencies() in all installed modules.

This function is similar to module_invoke_all(), with the main difference
that it does not require that a module be enabled to invoke its hook, only
that it be installed. This allows the update system to properly perform
updates even on modules that are currently disabled.

@return
  An array of return values obtained by merging the results of the
  hook_update_dependencies() implementations in all installed modules.

@see module_invoke_all()
@see hook_update_dependencies()
```

## Code

```php
function update_retrieve_dependencies() {
  $return = array();
  // Get a list of installed modules, arranged so that we invoke their hooks in
  // the same order that module_invoke_all() does.
  $modules = db_query("SELECT name FROM {system} WHERE type = 'module' AND schema_version <> :schema ORDER BY weight ASC, name ASC", array(':schema' => SCHEMA_UNINSTALLED))->fetchCol();
  foreach ($modules as $module) {
    $function = $module . '_update_dependencies';
    if (function_exists($function)) {
      $result = $function();
      // Each implementation of hook_update_dependencies() returns a
      // multidimensional, associative array containing some keys that
      // represent module names (which are strings) and other keys that
      // represent update function numbers (which are integers). We cannot use
      // array_merge_recursive() to properly merge these results, since it
      // treats strings and integers differently. Therefore, we have to
      // explicitly loop through the expected array structure here and perform
      // the merge manually.
      if (isset($result) && is_array($result)) {
        foreach ($result as $module => $module_data) {
          foreach ($module_data as $update => $update_data) {
            foreach ($update_data as $module_dependency => $update_dependency) {
              // If there are redundant dependencies declared for the same
              // update function (so that it is declared to depend on more than
              // one update from a particular module), record the dependency on
              // the highest numbered update here, since that automatically
              // implies the previous ones. For example, if one module's
              // implementation of hook_update_dependencies() required this
              // ordering:
              //
              // system_update_7001 ---> user_update_7000
              //
              // but another module's implementation of the hook required this
              // one:
              //
              // system_update_7002 ---> user_update_7000
              //
              // we record the second one, since system_update_7001() is always
              // guaranteed to run before system_update_7002() anyway (within
              // an individual module, updates are always run in numerical
              // order).
              if (!isset($return[$module][$update][$module_dependency]) || $update_dependency > $return[$module][$update][$module_dependency]) {
                $return[$module][$update][$module_dependency] = $update_dependency;
              }
            }
          }
        }
      }
    }
  }

  return $return;
}
```

---
_Drupal 7.103 · [includes/update.inc](https://github.com/drupal/drupal/blob/7.103/includes/update.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
