# drupal_depth_first_search()

- **Type:** Function
- **File:** [`includes/graph.inc`](_file.md), lines 47–72 · [local source](../../../source/includes/graph.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/graph.inc#L47-L72)

## Signature

```php
function drupal_depth_first_search(&$graph)
```

## Documentation

```text
Performs a depth-first search and sort on a directed acyclic graph.

@param $graph
  A three dimensional associated array, with the first keys being the names
  of the vertices, these can be strings or numbers. The second key is
  'edges' and the third one are again vertices, each such key representing
  an edge. Values of array elements are copied over.

  Example:
  @code
    $graph[1]['edges'][2] = 1;
    $graph[2]['edges'][3] = 1;
    $graph[2]['edges'][4] = 1;
    $graph[3]['edges'][4] = 1;
  @endcode

  On return you will also have:
  @code
    $graph[1]['paths'][2] = 1;
    $graph[1]['paths'][3] = 1;
    $graph[2]['reverse_paths'][1] = 1;
    $graph[3]['reverse_paths'][1] = 1;
  @endcode

@return
  The passed-in $graph with more secondary keys filled in:
  - 'paths': Contains a list of vertices than can be reached on a path from
    this vertex.
  - 'reverse_paths': Contains a list of vertices that has a path from them
    to this vertex.
  - 'weight': If there is a path from a vertex to another then the weight of
    the latter is higher.
  - 'component': Vertices in the same component have the same component
    identifier.

@see _drupal_depth_first_search()
```

## Code

```php
function drupal_depth_first_search(&$graph) {
  $state = array(
    // The order of last visit of the depth first search. This is the reverse
    // of the topological order if the graph is acyclic.
    'last_visit_order' => array(),
    // The components of the graph.
    'components' => array(),
  );
  // Perform the actual search.
  foreach ($graph as $start => $data) {
    _drupal_depth_first_search($graph, $state, $start);
  }

  // We do such a numbering that every component starts with 0. This is useful
  // for module installs as we can install every 0 weighted module in one
  // request, and then every 1 weighted etc.
  $component_weights = array();

  foreach ($state['last_visit_order'] as $vertex) {
    $component = $graph[$vertex]['component'];
    if (!isset($component_weights[$component])) {
      $component_weights[$component] = 0;
    }
    $graph[$vertex]['weight'] = $component_weights[$component]--;
  }
}
```

---
_Drupal 7.103 · [includes/graph.inc](https://github.com/drupal/drupal/blob/7.103/includes/graph.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
