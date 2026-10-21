# GraphUnitTest::assertComponents()

- **Type:** Method
- **File:** [`modules/simpletest/tests/graph.test`](../_file.md), lines 148–159 · [local source](../../../../../../source/modules/simpletest/tests/graph.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/graph.test#L148-L159)
- **Class:** [GraphUnitTest](../GraphUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function assertComponents($graph, $expected_components)
```

## Documentation

```text
Verify expected components in a graph.

@param $graph
  A graph array processed by drupal_depth_first_search().
@param $expected_components
  An array containing of components defined as a list of their vertices.
```

## Code

```php
  function assertComponents($graph, $expected_components) {
    $unassigned_vertices = array_fill_keys(array_keys($graph), TRUE);
    foreach ($expected_components as $component) {
      $result_components = array();
      foreach ($component as $vertex) {
        $result_components[] = $graph[$vertex]['component'];
        unset($unassigned_vertices[$vertex]);
      }
      $this->assertEqual(1, count(array_unique($result_components)), format_string('Expected one unique component for vertices @vertices, got @components', array('@vertices' => $this->displayArray($component), '@components' => $this->displayArray($result_components))));
    }
    $this->assertEqual(array(), $unassigned_vertices, format_string('Vertices not assigned to a component: @vertices', array('@vertices' => $this->displayArray($unassigned_vertices, TRUE))));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/graph.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/graph.test) · Licensed GPL-2.0-or-later (see LICENSE)._
