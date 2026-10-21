# update_resolve_dependencies()

- **Type:** Function
- **File:** [`includes/update.inc`](_file.md), lines 1232–1267 · [local source](../../../source/includes/update.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/update.inc#L1232-L1267)

## Signature

```php
function update_resolve_dependencies($starting_updates)
```

## Documentation

```text
Resolves dependencies in a set of module updates, and orders them correctly.

This function receives a list of requested module updates and determines an
appropriate order to run them in such that all update dependencies are met.
Any updates whose dependencies cannot be met are included in the returned
array but have the key 'allowed' set to FALSE; the calling function should
take responsibility for ensuring that these updates are ultimately not
performed.

In addition, the returned array also includes detailed information about the
dependency chain for each update, as provided by the depth-first search
algorithm in drupal_depth_first_search().

@param $starting_updates
  An array whose keys contain the names of modules with updates to be run
  and whose values contain the number of the first requested update for that
  module.

@return
  An array whose keys are the names of all update functions within the
  provided modules that would need to be run in order to fulfill the
  request, arranged in the order in which the update functions should be
  run. (This includes the provided starting update for each module and all
  subsequent updates that are available.) The values are themselves arrays
  containing all the keys provided by the drupal_depth_first_search()
  algorithm, which encode detailed information about the dependency chain
  for this update function (for example: 'paths', 'reverse_paths', 'weight',
  and 'component'), as well as the following additional keys:
  - 'allowed': A boolean which is TRUE when the update function's
    dependencies are met, and FALSE otherwise. Calling functions should
    inspect this value before running the update.
  - 'missing_dependencies': An array containing the names of any other
    update functions that are required by this one but that are unavailable
    to be run. This array will be empty when 'allowed' is TRUE.
  - 'module': The name of the module that this update function belongs to.
  - 'number': The number of this update function within that module.

@see drupal_depth_first_search()
```

## Code

```php
function update_resolve_dependencies($starting_updates) {
  // Obtain a dependency graph for the requested update functions.
  $update_functions = update_get_update_function_list($starting_updates);
  $graph = update_build_dependency_graph($update_functions);

  // Perform the depth-first search and sort the results.
  require_once DRUPAL_ROOT . '/includes/graph.inc';
  drupal_depth_first_search($graph);
  uasort($graph, 'drupal_sort_weight');

  foreach ($graph as $function => &$data) {
    $module = $data['module'];
    $number = $data['number'];
    // If the update function is missing and has not yet been performed, mark
    // it and everything that ultimately depends on it as disallowed.
    if (update_is_missing($module, $number, $update_functions) && !update_already_performed($module, $number)) {
      $data['allowed'] = FALSE;
      foreach (array_keys($data['paths']) as $dependent) {
        $graph[$dependent]['allowed'] = FALSE;
        $graph[$dependent]['missing_dependencies'][] = $function;
      }
    }
    elseif (!isset($data['allowed'])) {
      $data['allowed'] = TRUE;
      $data['missing_dependencies'] = array();
    }
    // Now that we have finished processing this function, remove it from the
    // graph if it was not part of the original list. This ensures that we
    // never try to run any updates that were not specifically requested.
    if (!isset($update_functions[$module][$number])) {
      unset($graph[$function]);
    }
  }

  return $graph;
}
```

---
_Drupal 7.103 · [includes/update.inc](https://github.com/drupal/drupal/blob/7.103/includes/update.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
