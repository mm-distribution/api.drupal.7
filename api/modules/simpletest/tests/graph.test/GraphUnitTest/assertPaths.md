# GraphUnitTest::assertPaths()

- **Type:** Method
- **File:** [`modules/simpletest/tests/graph.test`](../_file.md), lines 113–120 · [local source](../../../../../../source/modules/simpletest/tests/graph.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/graph.test#L113-L120)
- **Class:** [GraphUnitTest](../GraphUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function assertPaths($graph, $expected_paths)
```

## Documentation

```text
Verify expected paths in a graph.

@param $graph
  A graph array processed by drupal_depth_first_search().
@param $expected_paths
  An associative array containing vertices with their expected paths.
```

## Code

```php
  function assertPaths($graph, $expected_paths) {
    foreach ($expected_paths as $vertex => $paths) {
      // Build an array with keys = $paths and values = TRUE.
      $expected = array_fill_keys($paths, TRUE);
      $result = isset($graph[$vertex]['paths']) ? $graph[$vertex]['paths'] : array();
      $this->assertEqual($expected, $result, format_string('Expected paths for vertex @vertex: @expected-paths, got @paths', array('@vertex' => $vertex, '@expected-paths' => $this->displayArray($expected, TRUE), '@paths' => $this->displayArray($result, TRUE))));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/graph.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/graph.test) · Licensed GPL-2.0-or-later (see LICENSE)._
