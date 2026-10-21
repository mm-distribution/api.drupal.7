# _drupal_depth_first_search()

- **Type:** Function
- **File:** [`includes/graph.inc`](_file.md), lines 90–145 · [local source](../../../source/includes/graph.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/graph.inc#L90-L145)

## Signature

```php
function _drupal_depth_first_search(&$graph, &$state, $start, &$component = NULL)
```

## Documentation

```text
Performs a depth-first search on a graph.

@param $graph
  A three dimensional associated graph array.
@param $state
  An associative array. The key 'last_visit_order' stores a list of the
  vertices visited. The key components stores list of vertices belonging
  to the same the component.
@param $start
  An arbitrary vertex where we started traversing the graph.
@param $component
  The component of the last vertex.

@see drupal_depth_first_search()
```

## Code

```php
function _drupal_depth_first_search(&$graph, &$state, $start, &$component = NULL) {
  // Assign new component for each new vertex, i.e. when not called recursively.
  if (!isset($component)) {
    $component = $start;
  }
  // Nothing to do, if we already visited this vertex.
  if (isset($graph[$start]['paths'])) {
    return;
  }
  // Mark $start as visited.
  $graph[$start]['paths'] = array();

  // Assign $start to the current component.
  $graph[$start]['component'] = $component;
  $state['components'][$component][] = $start;

  // Visit edges of $start.
  if (isset($graph[$start]['edges'])) {
    foreach ($graph[$start]['edges'] as $end => $v) {
      // Mark that $start can reach $end.
      $graph[$start]['paths'][$end] = $v;

      if (isset($graph[$end]['component']) && $component != $graph[$end]['component']) {
        // This vertex already has a component, use that from now on and
        // reassign all the previously explored vertices.
        $new_component = $graph[$end]['component'];
        foreach ($state['components'][$component] as $vertex) {
          $graph[$vertex]['component'] = $new_component;
          $state['components'][$new_component][] = $vertex;
        }
        unset($state['components'][$component]);
        $component = $new_component;
      }
      // Only visit existing vertices.
      if (isset($graph[$end])) {
        // Visit the connected vertex.
        _drupal_depth_first_search($graph, $state, $end, $component);

        // All vertices reachable by $end are also reachable by $start.
        $graph[$start]['paths'] += $graph[$end]['paths'];
      }
    }
  }

  // Now that any other subgraph has been explored, add $start to all reverse
  // paths.
  foreach ($graph[$start]['paths'] as $end => $v) {
    if (isset($graph[$end])) {
      $graph[$end]['reverse_paths'][$start] = $v;
    }
  }

  // Record the order of the last visit. This is the reverse of the
  // topological order if the graph is acyclic.
  $state['last_visit_order'][] = $start;
}
```

---
_Drupal 7.103 · [includes/graph.inc](https://github.com/drupal/drupal/blob/7.103/includes/graph.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
