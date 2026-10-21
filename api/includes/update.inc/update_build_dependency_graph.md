# update_build_dependency_graph()

- **Type:** Function
- **File:** [`includes/update.inc`](_file.md), lines 1348–1385 · [local source](../../../source/includes/update.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/update.inc#L1348-L1385)

## Signature

```php
function update_build_dependency_graph($update_functions)
```

## Documentation

```text
Constructs a graph which encodes the dependencies between module updates.

This function returns an associative array which contains a "directed graph"
representation of the dependencies between a provided list of update
functions, as well as any outside update functions that they directly depend
on but that were not in the provided list. The vertices of the graph
represent the update functions themselves, and each edge represents a
requirement that the first update function needs to run before the second.
For example, consider this graph:

system_update_7000 ---> system_update_7001 ---> system_update_7002

Visually, this indicates that system_update_7000() must run before
system_update_7001(), which in turn must run before system_update_7002().

The function takes into account standard dependencies within each module, as
shown above (i.e., the fact that each module's updates must run in numerical
order), but also finds any cross-module dependencies that are defined by
modules which implement hook_update_dependencies(), and builds them into the
graph as well.

@param $update_functions
  An organized array of update functions, in the format returned by
  update_get_update_function_list().

@return
  A multidimensional array representing the dependency graph, suitable for
  passing in to drupal_depth_first_search(), but with extra information
  about each update function also included. Each array key contains the name
  of an update function, including all update functions from the provided
  list as well as any outside update functions which they directly depend
  on. Each value is an associative array containing the following keys:
  - 'edges': A representation of any other update functions that immediately
    depend on this one. See drupal_depth_first_search() for more details on
    the format.
  - 'module': The name of the module that this update function belongs to.
  - 'number': The number of this update function within that module.

@see drupal_depth_first_search()
@see update_resolve_dependencies()
```

## Code

```php
function update_build_dependency_graph($update_functions) {
  // Initialize an array that will define a directed graph representing the
  // dependencies between update functions.
  $graph = array();

  // Go through each update function and build an initial list of dependencies.
  foreach ($update_functions as $module => $functions) {
    $previous_function = NULL;
    foreach ($functions as $number => $function) {
      // Add an edge to the directed graph representing the fact that each
      // update function in a given module must run after the update that
      // numerically precedes it.
      if ($previous_function) {
        $graph[$previous_function]['edges'][$function] = TRUE;
      }
      $previous_function = $function;

      // Define the module and update number associated with this function.
      $graph[$function]['module'] = $module;
      $graph[$function]['number'] = $number;
    }
  }

  // Now add any explicit update dependencies declared by modules.
  $update_dependencies = update_retrieve_dependencies();
  foreach ($graph as $function => $data) {
    if (!empty($update_dependencies[$data['module']][$data['number']])) {
      foreach ($update_dependencies[$data['module']][$data['number']] as $module => $number) {
        $dependency = $module . '_update_' . $number;
        $graph[$dependency]['edges'][$function] = TRUE;
        $graph[$dependency]['module'] = $module;
        $graph[$dependency]['number'] = $number;
      }
    }
  }

  return $graph;
}
```

---
_Drupal 7.103 · [includes/update.inc](https://github.com/drupal/drupal/blob/7.103/includes/update.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
