# GraphUnitTest::testDepthFirstSearch()

- **Type:** Method
- **File:** [`modules/simpletest/tests/graph.test`](../_file.md), lines 28–88 · [local source](../../../../../../source/modules/simpletest/tests/graph.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/graph.test#L28-L88)
- **Class:** [GraphUnitTest](../GraphUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testDepthFirstSearch()
```

## Documentation

```text
Test depth-first-search features.
```

## Code

```php
  function testDepthFirstSearch() {
    // The sample graph used is:
    // 1 --> 2 --> 3     5 ---> 6
    //       |     ^     ^
    //       |     |     |
    //       |     |     |
    //       +---> 4 <-- 7      8 ---> 9
    $graph = $this->normalizeGraph(array(
      1 => array(2),
      2 => array(3, 4),
      3 => array(),
      4 => array(3),
      5 => array(6),
      7 => array(4, 5),
      8 => array(9),
      9 => array(),
    ));
    drupal_depth_first_search($graph);

    $expected_paths = array(
      1 => array(2, 3, 4),
      2 => array(3, 4),
      3 => array(),
      4 => array(3),
      5 => array(6),
      7 => array(4, 3, 5, 6),
      8 => array(9),
      9 => array(),
    );
    $this->assertPaths($graph, $expected_paths);

    $expected_reverse_paths = array(
      1 => array(),
      2 => array(1),
      3 => array(2, 1, 4, 7),
      4 => array(2, 1, 7),
      5 => array(7),
      7 => array(),
      8 => array(),
      9 => array(8),
    );
    $this->assertReversePaths($graph, $expected_reverse_paths);

    // Assert that DFS didn't created "missing" vertexes automatically.
    $this->assertFALSE(isset($graph[6]), 'Vertex 6 has not been created');

    $expected_components = array(
      array(1, 2, 3, 4, 5, 7),
      array(8, 9),
    );
    $this->assertComponents($graph, $expected_components);

    $expected_weights = array(
      array(1, 2, 3),
      array(2, 4, 3),
      array(7, 4, 3),
      array(7, 5),
      array(8, 9),
    );
    $this->assertWeights($graph, $expected_weights);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/graph.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/graph.test) · Licensed GPL-2.0-or-later (see LICENSE)._
