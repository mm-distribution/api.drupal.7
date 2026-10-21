# GraphUnitTest::assertWeights()

- **Type:** Method
- **File:** [`modules/simpletest/tests/graph.test`](../_file.md), lines 169–176 · [local source](../../../../../../source/modules/simpletest/tests/graph.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/graph.test#L169-L176)
- **Class:** [GraphUnitTest](../GraphUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function assertWeights($graph, $expected_orders)
```

## Documentation

```text
Verify expected order in a graph.

@param $graph
  A graph array processed by drupal_depth_first_search().
@param $expected_orders
  An array containing lists of vertices in their expected order.
```

## Code

```php
  function assertWeights($graph, $expected_orders) {
    foreach ($expected_orders as $order) {
      $previous_vertex = array_shift($order);
      foreach ($order as $vertex) {
        $this->assertTrue($graph[$previous_vertex]['weight'] < $graph[$vertex]['weight'], format_string('Weights of @previous-vertex and @vertex are correct relative to each other', array('@previous-vertex' => $previous_vertex, '@vertex' => $vertex)));
      }
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/graph.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/graph.test) · Licensed GPL-2.0-or-later (see LICENSE)._
