# GraphUnitTest::normalizeGraph()

- **Type:** Method
- **File:** [`modules/simpletest/tests/graph.test`](../_file.md), lines 93–103 · [local source](../../../../../../source/modules/simpletest/tests/graph.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/graph.test#L93-L103)
- **Class:** [GraphUnitTest](../GraphUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function normalizeGraph($graph)
```

## Documentation

```text
Return a normalized version of a graph.
```

## Code

```php
  function normalizeGraph($graph) {
    $normalized_graph = array();
    foreach ($graph as $vertex => $edges) {
      // Create vertex even if it hasn't any edges.
      $normalized_graph[$vertex] = array();
      foreach ($edges as $edge) {
        $normalized_graph[$vertex]['edges'][$edge] = TRUE;
      }
    }
    return $normalized_graph;
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/graph.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/graph.test) · Licensed GPL-2.0-or-later (see LICENSE)._
